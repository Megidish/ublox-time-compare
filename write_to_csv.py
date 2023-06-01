import csv
import os
 
def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
  
def write_to_csv(file_path, current_time_value, GPS_time_value, clock_zone_value,sync_precision):
    # Check if the file already exists
    file_exists = os.path.isfile(file_path)
    
    # Open the file in append mode with newline=''
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        calculated_latency = 32401
        drift = GPS_time_value - clock_zone_value - calculated_latency
        # Rewrite the file if it isnt empty
       
        # Write the header row only if the file doesn't exist
        if not file_exists:
            writer.writerow(['Current Time', 'GPS Time', 'clock.zone Time','Drift','clock.zone Sync Precision'])
        
        # Write the data row
        writer.writerow([current_time_value, GPS_time_value, clock_zone_value, drift,sync_precision])
        
        print(f"Data appended to '{file_path}' successfully in time '{current_time_value}' ")
 

