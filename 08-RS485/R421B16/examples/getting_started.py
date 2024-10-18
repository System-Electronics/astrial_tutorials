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

    print('Turn relay 1 on')
    check(board.on(1))
    time.sleep(1)

    print('Turn relay 1 off')
    check(board.off(1))
    time.sleep(1)

    print('Toggle relay 8')
    check(board.toggle(8))
    time.sleep(1)

    print('Latch relays 6 on, all other relays off')
    check(board.latch(6))
    time.sleep(1)

    print('Turn relay 4 on for 5 seconds, all other relays off')
    check(board.delay(4, delay=5))
    time.sleep(6)

    print('Turn relays 3, 7 and 8 on')
    check(board.toggle_multi([3, 7, 8]))
    time.sleep(1)

    print('Turn all relays on')
    check(board.on_all())
    time.sleep(1)

    print('Turn all relays off')
    check(board.off_all())
    time.sleep(1)
