import serial
import time
# when we run the code the com3 is used by python
# thus it is not free for arduino to use
arduino_obj = serial.Serial('com3', 115200)
def led(cmd):
    if cmd == "1":
        print('1')
        cmd = cmd+'\r'
        arduino_obj.write(cmd.encode())
        # led1.write(0)
    elif cmd == "0":
        print('0')
        cmd = cmd+'\r'
        arduino_obj.write(cmd.encode())
        # led1.write(1)
    else:
        print('more than 2 fingers')


while True:  # infinite loop

    # magic sauce :)
    cmd = input("enter the choice: ")
    led(cmd)
    # cmd = cmd+'\r'
    # arduino_obj.write(cmd.encode())
    # send it as a string
