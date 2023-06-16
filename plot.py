import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the data from the CSV file
data = pd.read_csv('updated_file.csv')

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

# Create a single figure with subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# Plot 1: Actual Drift vs. Predicted Drift
ax1.scatter(X_test['GPS Time'], y_test, label='Actual Drift')
ax1.scatter(X_test['GPS Time'], y_pred, label='Predicted Drift')
ax1.set_xlabel('GPS Time')
ax1.set_ylabel('Drift')
ax1.set_title('Actual Drift vs. Predicted Drift')
ax1.legend()

# Plot 2: Time Comparison
current_time = data['Current Time'].astype('datetime64[ns]')
drift = data['Drift'].astype('float')
ax2.plot(current_time, drift, marker='x', label='drift')
ax2.set_xlabel('Current Time')
ax2.set_ylabel('Time')
ax2.set_title('Time Comparison')
ax2.legend()

# Plot 3: Scatter plot of Number of SAT and Sync Precision
current_time = data['Current Time'].astype('datetime64[ns]')
num_sat = data['Number of SAT']
sync_precision = data['clock.zone Sync Precision']
ax3.scatter(current_time, num_sat, label='Number of SAT')
ax3.scatter(current_time, sync_precision, label='Sync Precision')
ax3.set_xlabel('Current Time')
ax3.set_ylabel('Value')
ax3.set_title('Data dependencies ')
ax3.legend()

# Adjust the spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()
