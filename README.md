# About the project
The project's purpose is to perform classification on a U-blox sensor to determine whether it is functioning correctly or faulty by subtracting its own timestamp tag from the timestamp tag of a time server.

# To install
install packages listed in a requirements.txt file using pip, you can use the following command:
```bash
pip install -r requirements.txt
```

# How to check which USB port are conncected to U-blox 
For mac users:
```bash
/dev && ls | grep tty.usbmodem
```
now go inside ublox_request_function.py and change u_blox_path to the output from eaarlier 
```python
u_blox_path = '/dev/enter here new path'
```
