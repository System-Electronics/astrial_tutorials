# Tutorial 01 - RGB Led Blink
## Material required
* 1 x Astrial
* 1 x CM4 carrier
* 1 x Breadboard
* 1 x RGB led
* 3 x 220Ω resistors
* 4 x Wire jumpers

## Setup
### Hardware setup
Connect the led, resistors and jumpers as shown in the following schematic.

![Schematic](images/schematic.png)

The Red, Green, and Blue lines of the led are connected to GPIO 25, GPIO 24, and GPIO 23 respectively, and Ground is connected to pin 20.

![GPIO Diagram](images/GPIO.png)

![Photo](images/photo.jpg)

### Install Python packages
Install the required python packages:
```
pip3 install -r requirements.txt
```

### Run the Python script
Run the RGB Led Blink script:
```
python3 rgb_led_blink.py
```

### GPIO Pins
The following table shows all the possible combinations of gpiochip and line that you can use in your code, and the corresponding GPIO.

| gpiochip  | line |  GPIO  |   |
|-----------|------|--------|---|
| gpiochip2 |   20 | GPIO0  |   |
| gpiochip2 |   19 | GPIO1  |   |
| gpiochip2 |   25 | GPIO2  |   |
| gpiochip2 |   21 | GPIO3  |   |
| gpiochip1 |   8  | GPIO4  |   |
| gpiochip1 |   9  | GPIO5  |   |
| gpiochip3 |  27  | GPIO6  | * |
| gpiochip3 |  26  | GPIO7  | * |
| gpiochip3 |  25  | GPIO13 | * |
| gpiochip3 |  24  | GPIO16 | * |
| gpiochip3 |  23  | GPIO17 | * |
| gpiochip4 |  13  | GPIO18 | * |
| gpiochip4 |  12  | GPIO19 | * |
| gpiochip4 |  11  | GPIO20 | * |
| gpiochip4 |  10  | GPIO21 | * |
| gpiochip1 |   0  | GPIO22 |   |
| gpiochip1 |   1  | GPIO23 |   |
| gpiochip1 |   2  | GPIO24 |   |
| gpiochip1 |   3  | GPIO25 |   |
| gpiochip1 |   4  | GPIO26 |   |
| gpiochip1 |   5  | GPIO27 |   |

\* only works with modified DTB

If you want to enable all available GPIOs, use the custom DTB provided in the `resources` directory (imx8mp-astrial.dtb)