import csv
import os.path

def write_to_csv(file_path, current_time_value, GPS_time_value, clock_zone_value):
    # Check if the file already exists
    file_exists = os.path.isfile(file_path)
    
    # Open the file in append mode with newline=''
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        calculated_latency = 32401
        drift = GPS_time_value - clock_zone_value - calculated_latency
        
        # Write the header row only if the file doesn't exist
        if not file_exists:
            writer.writerow(['Current Time', 'GPS Time', 'clock.zone Time','Drift'])
        
        # Write the data row
        writer.writerow([current_time_value, GPS_time_value, clock_zone_value, drift])
        
        print(f"Data appended to '{file_path}' successfully.")
 

