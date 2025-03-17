import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)
y = np.array([20, 30, 40, 50, 60, 70, 80, 90, 100, 110])

model = LinearRegression()
model.fit(X, y)

x = int(input("Enter a distance to get a fare: "))
predict_value = x 
predicted_y = model.predict(np.array([[predict_value]]))

print(f"Predicted value for {predict_value}: {predicted_y[0]:.0f}")

df = pd.DataFrame({'X': X.flatten(), 'y': y})

plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Heatmap of Features")
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(df['X'], df['y'], marker='o', linestyle='-', color='b')
plt.xlabel('X Values')
plt.ylabel('y Values')
plt.title('Time Series Plot')
plt.grid()
plt.show()

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='y', data=df, scatter_kws={"color": "red"}, line_kws={"color": "blue"})
plt.title("Scatter Plot with Regression Line")
plt.show()

sns.jointplot(x='X', y='y', data=df, kind='reg', height=6)
plt.show()

g = sns.FacetGrid(df, col="y", col_wrap=3, height=3)
g.map_dataframe(sns.scatterplot, x="X", y="y")
plt.show()
