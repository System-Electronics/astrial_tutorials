from sense_hat_astrial.stick import SenseStick
from sense_hat_astrial import SenseHat

# Create an instance of the SenseHat class
sense = SenseHat()
# Create an instance of the SenseStick class
stick = SenseStick()

# Define a callback function
def callback(event):
    if (event.action == "pressed" or event.action == "held"):
        # Display the direction on the LED matrix
        sense.show_letter(str(event.direction[0]).upper())
    else:
        sense.clear()

stick.direction_any = callback

input("Press Enter to exit...")
