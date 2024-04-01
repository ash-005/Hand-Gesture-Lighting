# from pyfirmata import Arduino
# comm = 'COM3'
# from serial import Serial
# import time
# arduino = Serial(port='COM3', baudrate=9600, timeout=0.1)


# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data


# while True:
#     num = input("Enter a number: ")
#     value = write_read(num)
#     print(value)


# board = Arduino('COM3')
# led1 = board.get_pin('d:13:o')


def led(total):
    if total == 0:
        print('0')
        # led1.write(0)

    elif total == 1:
        print('1')
        # led1.write(1)
    elif total == 2:
        print('2')
       # led1.write(0)
    else:
        print('more than 2 fingers')
       # led1.write(0)
