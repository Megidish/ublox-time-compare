import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
data = pd.read_csv('test.csv')

# Extract the columns
current_time = data['Current Time'].astype('datetime64[ns]')
gps_time = data['GPS Time'].astype('int64')
clock_zone_time = data['clock.zone Time'].astype('int64')


# Create the line chart
plt.plot(current_time, gps_time, marker='o', label='GPS Time')
plt.plot(current_time, clock_zone_time, marker='o', label='Clock Zone Time')

# Set chart title and axis labels
plt.title('Time Comparison')
plt.xlabel('Current Time')
plt.ylabel('Time')

# Show the legend
plt.legend()

# Display the chart
plt.show()
