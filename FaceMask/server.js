const express = require("express");
const multer = require("multer");
const { spawn } = require("child_process");
const fs = require("fs");
const path = require("path");

const app = express();
const port = 5000;

app.use(express.static("public"));

const upload = multer({ dest: "uploads/" });

app.post("/detect", upload.single("image"), (req, res) => {
    if (!req.file) {
        return res.status(400).json({ error: "No image uploaded" });
    }

    const imagePath = req.file.path;

    const pythonProcess = spawn("python", ["detect_mask.py", imagePath]);

    pythonProcess.stdout.on("data", (data) => {
        const result = data.toString().trim();
        res.json({ result });
    });

    pythonProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });

    pythonProcess.on("close", () => {
        fs.unlink(imagePath, (err) => {
            if (err) console.error("Error deleting file:", err);
        });
    });
});

app.listen(port, () => console.log(`Server running on http://localhost:${port}`));
