import sys
import torch
from PIL import Image
import cv2
import numpy as np

# Load the YOLOv5 model (Make sure to replace with the correct path)
model = torch.hub.load("ultralytics/yolov5", "custom", path=r"C:\\Users\\karan\\OneDrive\\Desktop\\Mask_Detection\\exp12\\weights\\best.pt", force_reload=True)

def detect_mask(image_path):
    img = Image.open(image_path)

    results = model(img)

    detected_classes = results.pandas().xyxy[0]['name'].tolist()

    if "mask" in detected_classes:
        print("Entry Allowed")
    else:
        print("Entry Not Allowed")

if __name__ == "__main__":
    image_path = sys.argv[1]
    detect_mask(image_path)
