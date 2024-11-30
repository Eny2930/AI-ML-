import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the data
try:
    data = pd.read_csv('house_prices.csv')
except FileNotFoundError:
    print("Error: The file 'house_prices.csv' was not found.")
    exit()

# Handling missing values (if any)
data = data.dropna(subset=['square_footage', 'number_of_bedrooms', 'price'])

# Feature engineering
X = data[['square_footage', 'number_of_bedrooms']]
y = data['price']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
try:
    # Ensure that the input data is valid
    if X_train.empty or y_train.empty:
        raise ValueError("Training data is empty.")
    model.fit(X_train, y_train)
except ValueError as e:
    print("Error: ", e)
    exit()

# Make predictions
try:
    y_pred = model.predict(X_test)
except Exception as e:
    print("Error: ", e)
    exit()

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)