# Tutorial 02 - RGB Led Blink Waveshare
The goal of this tutorial is the reproduce the results of Tutorial 01 on three different Waveshare boards.

## Required material
* 1 x Astrial
* 1 x Waveshare CM4-IO-BASE-A
* 1 x Waveshare CM4-IO-BASE
* 1 x Waveshare CM4 PoE Board (B)
* 1 x RGB led
* 3 x 220Ω resistors
* 4 x Wire jumpers

## Setup
The hardware and software setup is the same for all the boards, since they share the same pinout.

### Hardware setup
Connect the led, resistors and jumpers as shown in the following schematic.

![CM4 Base A/B schematic](images/schematic_cm4_base.png)
*CM4 Base A/B schematic*
![CM4 PoE schematic](images/schematic_cm4_poe.png)
*CM4 PoE schematic*

The Red, Green, and Blue lines of the led are connected to GPIO 25, GPIO 24, and GPIO 23 respectively, and Ground is connected to pin 20.

![GPIO Diagram](images/GPIO.png)

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
The following table shows all the possible combinations of gpiochip and line that you can use in your code, and the corresponding GPIO, using the default DTS. 

|  GPIO  | gpiochip  | line |   | PULL-UP CM4-IO-Base-A/B | PULL-UP CM4-POE |
|--------|-----------|------|---|:-----------------------:|:---------------:|
| GPIO0  | gpiochip2 |   20 |   |               X         |        X        |
| GPIO1  | gpiochip2 |   19 |   |               X         |        X        |
| GPIO2  | gpiochip2 |   25 |   |                         |        X        |
| GPIO3  | gpiochip2 |   21 |   |                         |        X        |
| GPIO4  | gpiochip1 |    8 |   |                         |                 |
| GPIO5  | gpiochip1 |    9 |   |                         |        X        |
| GPIO6  | gpiochip3 |   27 | * |                         |                 |
| GPIO7  | gpiochip3 |   26 | * |                         |                 |
| GPIO8  | gpiochip4 |    9 | * |                         |                 |
| GPIO9  | gpiochip4 |    8 | * |                         |                 |
| GPIO10 | gpiochip4 |    7 | * |                         |                 |
| GPIO11 | gpiochip4 |    6 | * |                         |                 |
| GPIO12 | gpiochip4 |    2 |   |                         |                 |
| GPIO13 | gpiochip4 |    5 |   |                         |                 |
| GPIO16 | gpiochip3 |   24 | * |                         |                 |
| GPIO17 | gpiochip3 |   23 | * |                         |                 |
| GPIO18 | gpiochip4 |   13 | * |                         |                 |
| GPIO19 | gpiochip4 |   12 | * |                         |                 |
| GPIO20 | gpiochip4 |   11 | * |                         |                 |
| GPIO21 | gpiochip4 |   10 | * |                         |                 |
| GPIO22 | gpiochip1 |    0 |   |                         |        X        |
| GPIO23 | gpiochip1 |    1 |   |                         |                 |
| GPIO24 | gpiochip1 |    2 |   |                         |                 |
| GPIO25 | gpiochip1 |    3 |   |                         |                 |
| GPIO26 | gpiochip1 |    4 |   |                         |                 |
| GPIO27 | gpiochip1 |    5 |   |                         |                 |


\* only works with modified DTS

If you want to enable all available GPIOs, use the custom DTB provided in the `resources` directory (imx8mp-astrial.dtb)