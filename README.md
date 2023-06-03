![U-blox_classification (3)](https://github.com/Megidish/ublox-time-compare/assets/105859276/51800d5a-41dd-4fa6-a4ca-c60898396037)
# About the project
The project's purpose is to perform classification on a U-blox sensor to determine whether it is functioning correctly or faulty by subtracting its own timestamp tag from the timestamp tag of a time server.

# What u-blox is ?
u-blox is a  high-performance GNSS (Global Navigation Satellite System) modules , offering precise positioning and navigation capabilities for various applications.
you can obtain accurate position, velocity, and time (PVT) data, including latitude, longitude, altitude, heading, speed, and precise timing information. These modules provide access to satellite signals from multiple GNSS constellations such as GPS, GLONASS, Galileo, BeiDou, and QZSS, enabling robust and reliable positioning information.

# Usage
Install packages listed in a requirements.txt file using pip, you can use the following command:
```bash
pip install -r requirements.txt
```

# How to check which USB port are conncected to U-blox 
For mac users enter to the terminal :
```bash
/dev && ls | grep tty.usbmodem
```
Now go inside ublox_request_function.py and change u_blox_path to the output from earlier 
```python
# Insted of this: 
u_blox_path = '/dev/tty.usbmodem112401'
# Enter the new USB port
u_blox_path = '/dev/enter here new path'
```

# Scraping data from website with selenium
this function is taken from main.py
```python
# Initializes a WebDriver instance with statement ensures that resources are properly released after execution
with webdriver.Chrome() as driver:
    try:
# Instructs the WebDriver to navigate to the specified website_URL
        driver.get(website_URL)
        clock_element = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, 'MyClockDisplay')))
        clock_stats_element = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'clock-stats')))
        
        while True:
# Parsing the data from the elements to the varibles that needed 
            web_timestamp = parsing_timestamp(clock_element)
            sync_precision = parsing_sync_precision(clock_stats_element)
            time.sleep(0.5)
# Allows for graceful termination of the script when u enter command + C
    except KeyboardInterrupt:
        pass
```

# Reading data from U-blox
This funcion is from ublox_request_functions.py
Inside this file u will find a functions that can help u to communicate with the U-blox :
```python
def get_timestamp_from_UBLOX():
    # Baudrate for communication with the u-blox device as 9600 
    baudrate = 9600
    # Initializing a serial connection to the device using the serial.Serial() function
    serial_port = serial.Serial(u_blox_path, baudrate, timeout=1)
    # Reads a line from the serial port
    reader = UBXReader(serial_port)
    data = serial_port.readline().decode().strip()
    # '$G' indicating that it is an NMEA message.
    if data.startswith('$G'):
        try:
            msg = pynmea2.parse(data)
        except pynmea2.ParseError:
            print(f"Failed to parse NMEA message: {data}")
    else:
        msg = reader.parse(data)
    output = parse_data_to_timestamp(str(msg))  
    return output
 ```
 
 # Mechine learning method 
The machine learning method used in our code is K-Nearest Neighbors (KNN) regression.
In this case, it is applied for regression to predict the "Drift" variable based on the features "GPS Time" and "clock.zone Time". 
To evaluate the performance of the model, the mean squared error (MSE) and R-squared score (R2) are calculated. MSE measures the average squared difference between the predicted and actual values, with lower values indicating better performance. R2 score measures the proportion of variance in the target variable explained by the model, with higher values indicating a better fit.

# Plot example for using KNN regression
