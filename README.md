# ublox-time-compare
This code help u get info from a U-blox with python and to scrape code from a time website that works like 1pps  



# How to check which port you are conncecting to U-blox for MAC users
enter this command: cd /dev && ls | grep tty.usbmodem
now enter the output inside ublox_request-function.py. \n
serial_port = serial.Serial('/dev/enter here output',baudrate, timeout =1)
