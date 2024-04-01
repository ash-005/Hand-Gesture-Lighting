import serial
import time
# when we run the code the com3 is used by python
# thus it is not free for arduino to
arduino_obj = serial.Serial('com3', 115200)
while True:  # infinite loop
    cmd = input("Enter the command: ")
    # magic sauce :)
    cmd = cmd+'\r'
    arduino_obj.write(cmd.encode())  # send it as a string
