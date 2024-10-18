# Control 8 leds using R421A08 relay board.
# Connect the LEDs to relays 1 to 8.

import time
import sys

# Add system path to find relay_ Python packages
sys.path.append('.')
sys.path.append('..')

import relay_modbus
import relay_boards

# Required: Configure serial port, for example:
#   On Linux:   '/dev/ttymxc2', '/dev/ttymxc0'
SERIAL_PORT = '/dev/ttymxc2'


def check(retval):
    if not retval:
        sys.exit(1)

def turn_relay_on_off(board, relay):
    print('Toggle relay {}'.format(relay))
    check(board.toggle(relay))
    time.sleep(1)
    check(board.toggle(relay))

if __name__ == '__main__':
    print('Getting started R421B16 relay board\n')

    # Create MODBUS object
    _modbus = relay_modbus.Modbus(serial_port=SERIAL_PORT)

    # Open serial port
    try:
        _modbus.open()
    except relay_modbus.SerialOpenException as err:
        print(err)
        sys.exit(1)

    # Create relay board object
    board = relay_boards.R421A08(_modbus, address=1)

    print('Status all relays:')
    check(board.print_status_all())
    time.sleep(1)

    turn_relay_on_off(board, 1)
    turn_relay_on_off(board, 2)
    turn_relay_on_off(board, 3)
    turn_relay_on_off(board, 4)
    turn_relay_on_off(board, 5)
    turn_relay_on_off(board, 6)
    turn_relay_on_off(board, 7)
    turn_relay_on_off(board, 8)
    turn_relay_on_off(board, 9)
    turn_relay_on_off(board, 10)
    turn_relay_on_off(board, 11)
    turn_relay_on_off(board, 12)
    turn_relay_on_off(board, 13)
    turn_relay_on_off(board, 14)
    turn_relay_on_off(board, 15)
    turn_relay_on_off(board, 16)

    print('Turn all relays on')
    check(board.on_all())
    time.sleep(1)

    print('Turn all relays off')
    check(board.off_all())
    time.sleep(1)
