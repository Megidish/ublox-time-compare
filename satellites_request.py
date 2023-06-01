import time
import datetime
import serial
from pyubx2 import UBXReader
baudrate = 9600

serial_port = serial.Serial('/dev/tty.usbmodem112401',baudrate, timeout =1)
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