from sense_hat_astrial import SenseHat
import time

# Create an instance of the SenseHat class
sense = SenseHat()

# Get the orientation, temperature, and humidity
while True:
    orientation = sense.get_orientation_degrees()
    print(orientation)

    temperature = sense.get_temperature()
    print(temperature)
    
    humidity = sense.get_humidity()
    print(humidity)
    
    time.sleep(0.2)