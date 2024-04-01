import cv2
import socket

from cvzone.HandTrackingModule import HandDetector

# NodeMCU IP address and port
nodemcu_ip = "NodeMCU_IP_Address"  # Replace with the actual IP address
nodemcu_port = 80

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.9, maxHands=1)

nodemcu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nodemcu_socket.connect((nodemcu_ip, nodemcu_port))

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
        count = str(count)
        count = count + '\r'
        nodemcu_socket.send(count.encode())  # Send the command to NodeMCU

    cv2.imshow("Hold UP your Fingers :)", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

nodemcu_socket.close()
cap.release()
cv2.destroyAllWindows()
