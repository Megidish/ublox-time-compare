import filecmp
import time
import datetime
import serial
from pyubx2 import UBXReader
import pynmea2

u_blox_path = '/dev/tty.usbmodem1201'

def parse_data_to_timestamp (sentence):
    fields = sentence.split(",")
    if fields[0] == "$GNRMC":
        timestamp = fields[1]
        return parse_to_UNIX(timestamp)

def parse_to_UNIX (timestamp):
    current_date = datetime.datetime.utcnow().date()
    timestamp_datetime = datetime.datetime.strptime(f"{current_date} {timestamp}", "%Y-%m-%d %H%M%S.%f")
    unix_timestamp = int(timestamp_datetime.timestamp())
    return unix_timestamp


def get_timestamp_from_UBLOX():
    baudrate = 9600
    serial_port = serial.Serial(u_blox_path, baudrate, timeout=1)

    reader = UBXReader(serial_port)
    data = serial_port.readline().decode().strip()

    if data.startswith('$G'):
        try:
            msg = pynmea2.parse(data)
            
        except pynmea2.ParseError:
            print(f"Failed to parse NMEA message: {data}")
    else:
        msg = reader.parse(data)
    output = parse_data_to_timestamp(str(msg))  
    return output

def get_sat_number_from_UBLOX():
    baudrate = 9600

    serial_port = serial.Serial(u_blox_path,baudrate, timeout =1)
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

    filecmp.close()
    print(f"timer expired 1 minutes have passed ")

def get_all_ublox_data():
    baudrate = 9600
    serial_port = serial.Serial(u_blox_path, baudrate, timeout=1)
    serial_port.isOpen()

    output=''
    for i in range(3):
        ubr = serial_port.readline().decode().strip()
        output+= ubr + '\n'


    timestamp  = None
    number_of_sat  = None
    fix_quality  = None

    for line in output.splitlines():
        splited_line = line.split(',')
        if splited_line[0] == '$GNRMC':
            timestamp = splited_line[1]
        if splited_line[0] == '$GNGGA':
            number_of_sat  = splited_line[7]
            fix_quality  =  splited_line[6]

    return parse_to_UNIX(timestamp) ,fix_quality,number_of_sat

