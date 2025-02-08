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

Lastly, connect an HDMI monitor: for this tutorial, to see the video stream, you need to connect a display to the CM4's HDMI port.

### Copy the example script
For this tutorial we are going to use a slightly modified version of the detection script that you will find on your newly flashed Astrial. The onlu difference is that we are going to use the `synchailonet` GStreamer component instead of the `hailonet` one.

We do this because the `hailonet` component is not able to handle the video stream coming from the Raspberry Pi Camera or any other CSI camera.

To use the modified version copy the `detection.sh` script to the Astrial, under the `/home/root/apps/detection` folder.

```sh
scp detection.sh root@<astrial_ip>:/home/root/apps/detection
```

You can elso edit yourself the detection script (`/home/root/apps/detection/detection.sh`) on your Astrial by changing the `hailonet` component with the `synchailonet` one at line 68.

### Software setup
After booting your Astrial go to `/opt/imx8-isp/bin` and launch the ISP media server in dual mode so that you can choose between CAM0 and CAM1 MIPI port (you still won't be able to use both of them simultaneously), while if you launch it in single mode only CAM0 will be usable.
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
