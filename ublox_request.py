import time
import datetime
import serial
from pyubx2 import UBXReader
import pynmea2

def parse_data_to_timestamp (sentence):
    fields = sentence.split(",")
    if fields[0] == "$GNRMC":
        timestamp = fields[1]
        return parse_to_UNIX(timestamp)
def parse_to_UNIX (timestamp):
    # Get the current date
    current_date = datetime.datetime.utcnow().date()

    # Combine the current date and the time stamp
    timestamp_datetime = datetime.datetime.strptime(f"{current_date} {timestamp}", "%Y-%m-%d %H%M%S.%f")

    # Convert to UNIX timestamp
    unix_timestamp = int(timestamp_datetime.timestamp())

    return unix_timestamp


def get_data_from_UBLOX():
    baudrate = 9600
    serial_port = serial.Serial('/dev/tty.usbmodem112301', baudrate, timeout=1)

    reader = UBXReader(serial_port)
    data = serial_port.readline().decode().strip()

    if data.startswith('$G'):
        try:
            msg = pynmea2.parse(data)
            
        except pynmea2.ParseError:
            print(f"Failed to parse NMEA message: {data}")
    else:
        msg = reader.parse(data)
        
    return parse_data_to_timestamp(str(msg))

