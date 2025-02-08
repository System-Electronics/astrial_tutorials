# Tutorial 03 - Sense Hat
## Material required
* 1 x Astrial
* 1 x CM4 carrier
* 1 x Sense Hat

## Setup
### Hardware setup
Connect the Sense Hat to the CM4's GPIO header, and the Astrial's 5V and GND to the 5V and GND pins of the USB header, as shown in the following schematic.

![Schematic](images/schematic.png)

### RTIMULib
The Sense HAT includes an IMU (Inertial Measurement Unit) sensor suite, for which you need the RTIMULib library.

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
pip3 install smbus2==0.4.3
```

### Copy the scripts
We provide a custom version of the `sense_hat` library called `sense_hat_astrial` in the main folder of this tutorial.
Copy the `sense_hat_astrial` folder to the Astrial, together with the example scripts.
```sh
scp -r sense_hat_astrial root@<ip_astrial>:/home/root
scp sense_hat_example.py root@<ip_astrial>:/home/root
```

### Run the Python script
Run the example script:
```sh
python3 sense_hat_example.py
```

![Photo](images/photo.jpg)

### Modify RTIMULib configuration
The first time you run the `imu_example.py` script, you may encounter an error like this:
```
OSError: Humidity Init Failed
```

This is because the default I2C bus used by the Sense Hat is 1, but the CM4 carrier uses bus 4.
To fix this, you need to modify the RTIMULib configuration file that is created automatically the first time you run the script.
Locate the `RTIMULib.ini` file inside `/home/root/.config/sense_hat`, and modify the I2CBus setting to `I2CBus=4`.