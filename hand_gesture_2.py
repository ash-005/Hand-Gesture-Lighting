import cv2
import serial
# import gesture_to_arduino as cont
# Using HandDetector module from mediapipe
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)  # Created cap object to initiate Video Capture
# detector object detects the hand (max 1) with confidence threshold of 0.9
detector = HandDetector(detectionCon=0.9, maxHands=1)

# Arduino_obj to initial the Serial communication over the specific communication channel
arduino_obj = serial.Serial('com9', 115200)
# creating an infinite loop
while True:
    # store the ret frame from the video
    ret, frame = cap.read()
    # flips the frame
    frame = cv2.flip(frame, 1)
    # using findHands we detect number of hands storing it in 'hands'
    hands, frame = detector.findHands(frame)
    if not hands:
        # if no hands detected
        pass
        # print("Nothing on screen")
    else:
        # Storing the hands first element in hands1 obj
        hands1 = hands[0]
        fingers = detector.fingersUp(hands1)
        # stores the count of fingers held up by the user
        count = fingers.count(1)
        # Converting the variable to string datatype so that it can be modified to be encoded and sent over serial communication
        count = str(count)
        # Adding '\r' to get the carriage return character
        count = count+'\r'
        # Writing encoded bytes
        arduino_obj.write(count.encode())
    # Pass the number of fingers to gesture_to_arduino.py led(cmd) function
    # cont.led(count)

    # print(fingers)
    #
    cv2.imshow("Hold UP your Fingers :)", frame)
    # To terminate the frame press ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
