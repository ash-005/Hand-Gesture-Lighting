import serial
import time

ser = serial.Serial('com4', 115200, timeout=5)

# Function to send data to NodeMCU


def send_data(data):
    # Encode the data as bytes before sending
    encoded_data = data.encode('utf-8')
    ser.write(encoded_data)
    print(f"Sent: {data}")


if __name__ == "__main__":
    try:
        while True:
            # Get input from the user (or any other data source)
            data_to_send = input("Enter data to send (or 'exit' to quit): ")

            # Send the data to NodeMCU
            send_data(data_to_send)

            # Exit the loop if the user enters 'exit'
            if data_to_send.lower() == 'exit':
                break

    except KeyboardInterrupt:
        print("Keyboard Interrupt. Exiting...")
    finally:
        # Close the serial connection
        ser.close()
