import serial
import time

# Function to set up the serial connection
def setup_serial(port='COM5', baudrate=115200, timeout=1):
    try:
        ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        print(f"Connected to {port} at {baudrate} baud.")
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

# Function to send data
def send_data(ser, data):
    ser.write(data.encode())  # Send data as bytes
    print(f"Sent: {data}")

# Function to read data from STM32
def read_data(ser):
    if ser.in_waiting > 0:  # Check if data is available to read
        received = ser.readline().decode('utf-8').strip()  # Read line and decode
        print(f"Received: {received}")

# Main function to run the example
def main():
    ser = setup_serial()  # Initialize serial connection
    if ser is None:
        return  # Exit if serial setup failed

    try:
        while True:
            send_data(ser, "Hello STM32!")  # Send string data
            time.sleep(1)
            read_data(ser)  # Read any response from STM32
            time.sleep(1)  # Wait a second
    except KeyboardInterrupt:
        print("Interrupted by user")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the serial connection
        if ser is not None:
            ser.close()
            print("Serial connection closed.")

if __name__ == "__main__":
    main()
