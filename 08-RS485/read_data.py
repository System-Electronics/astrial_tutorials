import serial
import time
import argparse

def main():
    parser = argparse.ArgumentParser(description='Serial port communication.')
    parser.add_argument('--dev', type=str, required=True, help='Port for the serial communication')
    args = parser.parse_args()

    serialPort = serial.Serial(
        port=args.dev, baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
    )
    serialString = ""  # Used to hold data coming over UART

    while True:
        # Read data out of the buffer until a carriage return / new line is found
        serialString = serialPort.readline()

        # Print the contents of the serial data
        try:
            print(serialString.decode("Ascii"))
        except:
            pass

if __name__ == "__main__":
    main()
