# Tutorial 03 - Sense Hat
## Material required
* 1 x Astrial
* 1 x CM4 carrier
* 1 x Sense Hat

## Setup
### Hardware setup
Connect the Sense Hat to the CM4's GPIO header, and the Astrial 5V and GND to the 5V and GND pins of the USB header, like in the following schematic.

![Schematic](images/schematic.png)

### Use custom DTB
To enable the Sense Hat functionalities, you need to use the custom DTB provided in the `resources` folder.
For instructions on using a custom DTB, see [Use a custom DTB](./../README.md#use-a-custom-dtb).

To enable I2C on Astrial we edited the DTS like this:
```dts
&i2c5 {
    clock-frequency = <100000>;
    pinctrl-names = "default";
    pinctrl-0 = <&pinctrl_i2c5>;
    status = "okay";
};

&i2c6 {
    clock-frequency = <100000>;
    pinctrl-names = "default";
    pinctrl-0 = <&pinctrl_i2c6>;
    status = "okay";

    ...
};
...
pinctrl_i2c5: i2c5grp {
    fsl,pins = <
        MX8MP_IOMUXC_SAI5_RXD0__I2C5_SCL	0x400001c2
        MX8MP_IOMUXC_SAI5_MCLK__I2C5_SDA	0x400001c2
    >;
};

pinctrl_i2c6: i2c6grp {
    fsl,pins = <
        MX8MP_IOMUXC_SAI5_RXFS__I2C6_SCL	0x400001c2
        MX8MP_IOMUXC_SAI5_RXC__I2C6_SDA	    0x400001c2
    >;
};
```
For a complete overview of the changes made to the DTS, see the `resources` folder.

### RTIMULib
Download and build [RTIMULib](https://github.com/RPi-Distro/RTIMULib/tree/master/Linux/python):
1. Clone the repository on your host device:
```sh
git clone https://github.com/RPi-Distro/RTIMULib.git
```
2. Copy the repository on your Astrial:
```sh
scp -r RTIMULib root@<ip_astrial>:/home/root/
```
3. Build the library on your Astrial:
```sh
cd RTIMULib/Linux/python
python3 setup.py build
sudo python3 setup.py install
```

### Install Python packages
Install the required Python packages:
```sh
pip3 install -r requirements.txt
```

We provide a custom version of the `sense_hat` library called `sense_hat_astrial` in the main folder of this tutorial.
Copy the `sense_hat_astrial` folder to the Astrial, together with the example scripts.

### Run the Python script
Run the example script:
```sh
python3 sense_hat_example.py
```

### Modify RTIMULib configuration
The first time you run the `imu_example` script, you may encounter an error like this:
```
OSError: Humidity Init Failed
```

This is because the default I2C bus used by the Sense Hat is 1, but the CM4 carrier uses bus 4.
To fix this, you need to modify the RTIMULib configuration file that is created automatically the first time you run the script.
Locate the `RTIMULib.ini` file inside `/home/root/.config/sense_hat`, and modify the I2CBus setting to `I2CBus=4`.


![Photo](images/photo.jpg)