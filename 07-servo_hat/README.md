# Tutorial 07 - Servo hat
## Required material
* 1 x Astrial
* 1 x CM4 carrier
* 1 x Adafruit 16-Channel PWM / Servo HAT
* 1 x LED
* 1 x 220Ω resistor
* 2 x F/M jumper wires
* 1 x Breadboard
* 1 x Positional servo motor
* 4 x Continuous servo motor \[even though 1 is enough\]

## Setup
### Hardware setup

Let's start by preparing the necessary hardware components:

* First connect the PWM / Servo Hat to the GPIO header of your CM4 board. You might need to solder the hat to its pin extension in order to make it work properly.
* Connect the LED to channel 0 of the Hat with the 220Ω resistor.
* Connect the continuous servos to channel 1 to 4.
* Connect the positional servo to channel 5.

### Install Python packages
Install the required python packages:
```
pip3 install PCA9685-driver==1.2.0
```

### Run the Python script
Copy the python script of this tutorial, along with the PCA9685 library, to the Astrial. Then, run the example script:

```sh
python3 example.py
```

You should see first the LED blinking smoothly for 4 times, then the continuous servos rotating back and forth at maximum speed and finally the positional servo motor rotating from 0° to 180° twice.

![Final result](images/animazione.gif)