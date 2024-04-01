import serial
import time

arduinoData = serial.Serial('com3', 115200)
# object to read data from
time.sleep(1)

while True:
    while (arduinoData.inWaiting() == 0):
        pass
    dataPac = arduinoData.readline()
    dataPac = str(dataPac, 'utf-8')  # covert to string
    dataPac = dataPac.strip('\r\n')
    splitPac = dataPac.split(",")

    x = (splitPac[0])
    y = (splitPac[1])
    z = (splitPac[2])

    print("X = ", x, "Y = ", y, "Z = ", z)
