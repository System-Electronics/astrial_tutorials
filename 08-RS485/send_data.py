import serial
import argparse
import time

def main():
    parser = argparse.ArgumentParser(description='Serial port communication.')
    parser.add_argument('--dev', type=str, required=True, help='Device path of the serial port')
    args = parser.parse_args()

    serial_port = serial.Serial(port=args.dev, baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    
    while True:
        serial_port.write(b"Hello World \r\n")
        time.sleep(1)
if __name__ == "__main__":
    main()
