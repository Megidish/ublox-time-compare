import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data from CSV file
data = pd.read_csv('test.csv')

# Extract features and labels
X = data['Drift'].values.reshape(-1, 1)
y = data['Current Time'].values.reshape(-1, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Reshape y_train and y_test
y_train = y_train.ravel()
y_test = y_test.ravel()

# Create and train the K-Nearest Neighbors classifier
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Predict the labels for the test set
y_pred = knn.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Plotting the data and decision boundary
x_boundary = np.linspace(np.min(X), np.max(X), 100).reshape(-1, 1)
y_boundary = knn.predict(x_boundary)

plt.scatter(X_train, y_train, color='blue', label='Training Data')
plt.scatter(X_test, y_test, color='green', label='Test Data')
plt.plot(x_boundary, y_boundary, color='red', label='Decision Boundary')

plt.xlabel('Drift')
plt.ylabel('Timestamp')
plt.title('K-Nearest Neighbors Classification')
plt.legend()
plt.show()
