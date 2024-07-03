import serial 
import time

# the below code block can also be used if there are errors with the arduino declaration and initialization
#arduino = serial.Serial('/dev/ttyACM0, 115200, timeout=5)

arduino = serial.Serial(
    port = 'dev/ttyACM0',
    baudrate = 115200,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    timeout = 5,
    xonxoff = False,
    rtscts = False,
    dsrdtr = False,
    write_timeout = 2
)

while True:
    try: 
        # sends the command to arduino and encodes that command in a format for arduino to process
        arduino.write("Command from Jetson|".encode())

        # the encoded message is now with arduino

        # reads that data that is send back from the arduino
        data = arduino.readline()
        if data: # if arduino has send back data it reads the data and prints it
            print(data)
        time.sleep(1)
    except Exception as e: 
        print(e)
        arduino.close()
