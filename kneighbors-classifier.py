import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the data from the CSV file
data = pd.read_csv('test.csv')

# Extract the features and target variable
X = data[['GPS Time', 'clock.zone Time']] 
y = data['Drift']  

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the KNN regressor
knn = KNeighborsRegressor(n_neighbors=1)   
knn.fit(X_train, y_train)

# Predict the target variable for the test set
y_pred = knn.predict(X_test)

# Evaluate the performance of the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Create a scatter plot of the data
plt.scatter(X_test['GPS Time'], y_test, label='Actual Drift')
plt.scatter(X_test['GPS Time'], y_pred, label='Predicted Drift')

plt.xlabel('GPS Time')
plt.ylabel('Drift')
plt.title('Actual Drift vs. Predicted Drift')
plt.legend()
plt.show()
