import cv2
import serial
# import gesture_to_arduino as cont
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=1)
arduino_obj = serial.Serial('com3', 115200)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hands, frame = detector.findHands(frame)
    if not hands:
        pass
        # print("Nothing on screen")
    else:
        hands1 = hands[0]
        fingers = detector.fingersUp(hands1)
        count = fingers.count(1)
        count = str(count)
        count = count+'\r'
        arduino_obj.write(count.encode())
    # Pass the number of fingers to gesture_to_arduino.py led(cmd) function
    # cont.led(count)

    # print(fingers)
    cv2.imshow("FRAME", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
