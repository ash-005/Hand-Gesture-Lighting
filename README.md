# Hand Gesture Recognition LED Glow System

This project implements a hand gesture recognition system using OpenCV, Serial communication, and an Arduino Uno to control LEDs based on the number of fingers held up.

## Overview

The system captures live video feed from a camera using OpenCV and processes it to detect hand gestures. The hand detector module identifies the number of fingers held up by the user. This data is then sent to an Arduino Uno board via Serial communication. Based on the detected number of fingers, corresponding LEDs are lit up, creating a visual representation of the hand gesture.

## Features

- Real-time hand gesture recognition using OpenCV.
- Communication between Python and Arduino Uno via Serial.
- LED control based on the number of fingers detected.
- Simple and intuitive user interface.

## Requirements

- Python 3.x
- OpenCV
- pySerial
- Arduino IDE
- Arduino Uno board
- LEDs and resistors for visual feedback

## Usage

1. Connect the camera to your computer and ensure it is properly detected.
2. Upload the Arduino sketch (`arduino_code.ino`) to the Arduino Uno board.
3. Install the required Python libraries (`opencv`, `pyserial`).
4. Run the Python script (`hand_gesture.py`) to start the hand gesture recognition system.
5. Hold up fingers in front of the camera to see the corresponding LEDs light up based on the detected gesture.

## Files Included

- `hand_gesture_recognition.py`: Python script for hand gesture recognition.
- `hand_detector.py`: Hand detection module.
- `arduino_code.ino`: Arduino Uno sketch for LED control.
- `README.md`: Documentation and instructions (you're reading it!).

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or improvements, feel free to submit a pull request.

