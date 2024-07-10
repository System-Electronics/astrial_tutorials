import time
from gpiod.line import Direction, Value
import gpiod

# Define the GPIO lines for the RGB LED
RED_LINE = 3
GREEN_LINE = 2
BLUE_LINE = 1

# Define the GPIO device
GPIO_DEVICE = "/dev/gpiochip1"

# Ensure the GPIO device is valid
assert gpiod.is_gpiochip_device(GPIO_DEVICE)

# Request control over the GPIO lines with initial settings
with gpiod.request_lines(
    GPIO_DEVICE,
    consumer="blink-example",
    config={
        # Configure the red LED line as output and initially inactive
        RED_LINE: gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.INACTIVE
        ),
        # Configure the green LED line as output and initially inactive
        GREEN_LINE: gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.INACTIVE
        ),
        # Configure the blue LED line as output and initially inactive
        BLUE_LINE: gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.INACTIVE
        ),
    },
) as request:
    # Loop indefinitely to blink the RGB LED
    while True:
        # Activate the red LED
        request.set_value(RED_LINE, Value.ACTIVE)
        time.sleep(0.5)  # Wait for 0.5 seconds
        # Deactivate the red LED
        request.set_value(RED_LINE, Value.INACTIVE)

        # Activate the green LED
        request.set_value(GREEN_LINE, Value.ACTIVE)
        time.sleep(0.5)  # Wait for 0.5 seconds
        # Deactivate the green LED
        request.set_value(GREEN_LINE, Value.INACTIVE)

        # Activate the blue LED
        request.set_value(BLUE_LINE, Value.ACTIVE)
        time.sleep(0.5)  # Wait for 0.5 seconds
        # Deactivate the blue LED
        request.set_value(BLUE_LINE, Value.INACTIVE)