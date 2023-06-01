import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV file into a DataFrame
data = pd.read_csv('test.csv')

# Extract the columns
current_time = data['Current Time'].astype('datetime64[ns]')
drift = data['Drift'].astype('float')

# Create the line chart
plt.plot(current_time, drift, marker='x', label='drift')

# Set chart title and axis labels
plt.title('Time Comparison')
plt.xlabel('Current Time')
plt.ylabel('Time')

# Show the legend
plt.legend()

# Display the chart
plt.show()
