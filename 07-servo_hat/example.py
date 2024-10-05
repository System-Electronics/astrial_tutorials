import time
from PCA9685.servo import *
from PCA9685 import PCA9685

# Create a simple PCA9685 class instance.
pca = PCA9685()

pca.frequency = 50

# We make the LED blink ON and OFF smoothly for 4 times before moving on
for k in range(4):
    for i in range(0, 0xFFFF, 100):
        pca.channels[0].duty_cycle = i


    for i in range(0xFFFF, 0, -100):
        pca.channels[0].duty_cycle = i

# We initialise 4 continuous servos with channels 1, 2, 3 and 4, and a positional servo on channel 5
continuousArray = [ContinuousServo(pca.channels[i]) for i in range(1, 5)]
positional = Servo(pca.channels[5])

# We first rotate the servos at full speed in clockwise direction
for continuous in continuousArray:
    continuous.throttle = 1
time.sleep(2)
# And then we make them spin in the opposite direction
for continuous in continuousArray:
    continuous.throttle = -1
time.sleep(2)
# And finally we stop all of them
for continuous in continuousArray:
    continuous.throttle = 0

# We make the positional servo rotate from 0 to 180 degrees and back
for i in range(180):
    positional.angle = i
    time.sleep(0.03)
for i in range(180):
    positional.angle = 180 - i
    time.sleep(0.03)

# We do the same thing but with the fractional angle
fraction = 0.0
while fraction < 1.0:
    positional.fraction = fraction
    fraction += 0.01
    time.sleep(0.03)