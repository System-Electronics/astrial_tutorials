from sense_hat_astrial import SenseHat
import time

# Create an instance of the SenseHat class
sense = SenseHat()

# Get the orientation, temperature, and humidity
while True:
    orientation = sense.get_orientation_degrees()
    print("Orientation:", orientation)

    temperature = sense.get_temperature()
    print("Temperature:", temperature)
    
    humidity = sense.get_humidity()
    print("Humidity:", humidity)

    pressure = sense.get_pressure()
    print("Pressure:", pressure)
    
    time.sleep(0.2)