import cv2
import serial
from cvzone.HandTrackingModule import HandDetector

# Initialize video capture
cap = cv2.VideoCapture(0)
# Initialize hand detector
detector = HandDetector(detectionCon=0.9, maxHands=1)

# Initialize serial communication with Arduino
arduino_obj = serial.Serial('com3', 115200)

# Define LED control commands for each gesture
gestures = {
    "Fist": "0000",          # All LEDs OFF
    "One Finger": "1000",     # Turn ON LED 1
    "Two Fingers": "0100",    # Turn ON LED 2
    "Three Fingers": "0010",  # Turn ON LED 3
    "Four Fingers": "0001",   # Turn ON LED 4
    "Five Fingers": "1111",   # All LEDs ON
    "Peace Sign": "0110",     # Turn ON LED 2 and 3
    "Thumb Up": "1001",      # Turn ON LED 1 and 4
    "OK Sign": "0011"         # Turn ON LED 3 and 4
}

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hands, frame = detector.findHands(frame)

    if not hands:
        pass
    else:
        hands1 = hands[0]
        fingers = detector.fingersUp(hands1)
        count = fingers.count(1)

        # Determine the gesture based on finger count
        if count == 0:
            gesture = "Fist"
        elif count == 1:
            gesture = "One Finger"
        elif count == 2:
            gesture = "Two Fingers"
        elif count == 3:
            gesture = "Three Fingers"
        elif count == 4:
            gesture = "Four Fingers"
        elif count == 5:
            gesture = "Five Fingers"
        else:
            # Additional gestures
            if fingers[1] == 1 and fingers[2] == 1:
                gesture = "Peace Sign"
            elif fingers[0] == 1 and fingers[4] == 1:
                gesture = "Thumb Up"
            else:
                gesture = "OK Sign"

        # Send the corresponding LED control command to Arduino
        led_command = gestures.get(gesture, "0000")
        arduino_obj.write(led_command.encode())

    cv2.imshow("Gesture Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
