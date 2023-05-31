import pandas as pd
import matplotlib.pyplot as plt
# Read the CSV file into a DataFrame
data = pd.read_csv('test.csv')

# Extract the columns
current_time = data['Current Time'].astype('datetime64[ns]')
gps_time = data['GPS Time'].astype('int64')
clock_zone_time = data['clock.zone Time'].astype('int64')

gps_time =clock_zone_time - gps_time

# Create the line chart
plt.plot(current_time, abs(gps_time), marker='x', label='drift')

# Set chart title and axis labels
plt.title('Time Comparison')
plt.xlabel('Current Time')
plt.ylabel('Time')

# Show the legend
plt.legend()

# Display the chart
plt.show()
