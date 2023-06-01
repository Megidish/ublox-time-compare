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
            print(msg)
            
        except pynmea2.ParseError:
            print(f"Failed to parse NMEA message: {data}")
    else:
        msg = reader.parse(data)
        
    return parse_data_to_timestamp(str(msg))

def get_sat_number_from_UBLOX():
    baudrate = 9600

    serial_port = serial.Serial('/dev/tty.usbmodem112301',baudrate, timeout =1)
    serial_port.isOpen()
    raw_data = open('data.txt', 'w')

    parsed_data = open('parsed_data.txt', 'w')

    reader = UBXReader(serial_port)
    print("Timer start for 1 minutes")



    time_now = datetime.datetime.now()

    # current_time = time_now.strftime("%H :%M,:%S")
    f_time = time_now + datetime.timedelta(minutes=2)



    while datetime.datetime.now() < f_time:
        ubr = serial_port.readline().decode().strip()
        raw_data.write(ubr + '\n')
        #enter the  ubr to file

        msg = reader.parse(ubr)

        if msg:

            if msg.name == 'NAV-POSLIH':
                lat = msg.payload.lat
                lon = msg.payload.lon
                height = msg.payload.height

                num_sv = msg.payload.numSV

                azimuth = msg.payload.heading
                parsed_data.write(f"lat:{lat}, lon:{lon},height{height},num_sv{num_sv},azimuth{azimuth}")
            else:
                parsed_data.write("Dont work",ubr + '\n')
                time.sleep(1)

    raw_data.close()
    parsed_data.close()

    print("timer expired for 1 minutes")

    file.close()
    print(f"timer expired 1 minutes have passed ")
