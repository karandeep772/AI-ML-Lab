import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Load dataset
HouseDF = pd.read_csv('USA_Housing.csv')

# Display dataset info
print(HouseDF.info())

# Exclude non-numeric columns for correlation
numeric_df = HouseDF.select_dtypes(include=['float64', 'int64'])

# Check correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

# Selecting features and target variable
X = numeric_df.drop(columns=['Price'])  # Exclude the target variable
y = HouseDF['Price']

# Standardizing features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.4, random_state=101)

# Train Linear Regression Model
lm = LinearRegression()
lm.fit(X_train, y_train)

# Model Intercept and Coefficients
print(f"Intercept: {lm.intercept_}")
coeff_df = pd.DataFrame(lm.coef_, index=X.columns, columns=['Coefficient'])
print(coeff_df)

# Predictions
predictions = lm.predict(X_test)

# Scatter plot of actual vs predicted prices
plt.figure(figsize=(8, 5))
plt.scatter(y_test, predictions, alpha=0.5)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")
plt.show()

# Fixed: Using histplot instead of distplot
plt.figure(figsize=(8, 5))
sns.histplot((y_test - predictions), bins=50, kde=True)
plt.title("Residuals Distribution")
plt.show()

# Model Evaluation Metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))