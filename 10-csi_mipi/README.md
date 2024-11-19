# Tutorial 10 - CSI/MIPI
## Material required
* 1 x Astrial
* 1 x CM4 carrier
* 1 x Raspberry Pi Camera Module 2
* 1 x RPI CAMERA CABLE STANDARD-MINI
* 2 x Jumper wires (F/F)

## Setup
### Hardware setup

First you need to fit 2 jumpers on J6 as shown in the image below to enable CAM0
![J6 Jumper](images/j6_jumpers.jpg)

Connect you Raspberry Pi Camera to the CM4 Carrier board using either CAM0 or CAM1 port using RPI CAMERA CABLE STANDARD-MINI-300MM.
![RPI Camera connected to CM4 using adapter cable](images/RPi-Camera-CM4.jpg)

### Copy the example script
If you have previously modified the detection script on you Astrial, copy the `detection.sh` script to the Astrial, under the `/home/root/apps/detection` folder. This script uses the raspberry camera to detect objects and display the video stream on the screen.

```sh
scp detection.sh root@<astrial_ip>:/home/root/apps/detection
```

### Software setup
After booting your Astrial go to /opt/imx8-isp/bin and launch the ISP media server in dual mode so that you can choose between CAM0 and CAM1 MIPI port (you still won't be able to use both of them simultaneously), while if you launch it in single mode only CAM0 will be usable.
```sh
cd /opt/imx8-isp/bin
./run.sh -lm -c dual_imx219_1080p60 &
```
Then go back to the detection script directory and run the script
```sh
cd /home/root/apps/detection
./detection.sh -i /dev/<video device>
```
Replace `<video device>` either with video2 or video3 if you are using CAM0 or CAM1
