# About the project
The project's purpose is to perform classification on a U-blox sensor to determine whether it is functioning correctly or faulty by subtracting its own timestamp tag from the timestamp tag of a time server.

# To install
install packages listed in a requirements.txt file using pip, you can use the following command:
```bash
pip install -r requirements.txt
```

# How to check which port you are conncecting to U-blox for MAC users
enter this command: cd /dev && ls | grep tty.usbmodem
now enter the output inside ublox_request-function.py. 
serial_port = serial.Serial('/dev/enter here output',baudrate, timeout =1)
