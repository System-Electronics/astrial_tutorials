# Astrial Tutorials
Welcome to the Astrial Tutorials repository. This repository contains various tutorials designed to help users get acquainted with the Astrial platform and its features. Each folder in this repository contains a specific tutorial.

## Getting Started
To get started with the tutorials, you will need to clone this repository to your local machine:

```sh
git clone https://github.com/System-Electronics/astrial_tutorials.git
```

Each tutorial is self-contained within its own folder. Navigate to the folder of the tutorial you want to start with and follow the instructions in the README.md file within that folder.

### Build Yocto image
Follow the official System Elecronics guide to build the Astrial Yocto image:
https://github.com/System-Electronics/meta-sysele-nxp-5.15.71/blob/main/ASTRIAL-YOCTO-INSTALL.md

### Flash SD Card
Flash the SD Card using the following command (replace \<sdx\> with the name of your SD Card):  
```
cd <astrial_build_directory>/build/tmp/deploy/images/astrial-imx8mp/
zstdcat system-astrial-image-astrial-imx8mp.wic.zst | sudo dd of=/dev/<sdx> bs=1M conv=fsync
```

## Select a dtb
To select a Device Tree Blob (DTB) for the Astrial, follow these steps:
1. Connect your PC to the Astrial using a TTY-USB cable.
2. Connect to the Astrial using a serial terminal emulator with a baudrate of 115200. We use `tio` in this example:
```sh
sudo tio /dev/ttyUSB0 -b 115200
```
3. Power on the Astrial.
4. Press any key to stop the boot process during the first seconds of the boot process. If you couldn't stop the boot process, reboot the Astrial and try again.
5. Run the following commands to select the DTB:
```sh
setenv fdtfile 'your_dtb'.dtb
saveenv
```
6. To make sure the DTB is correctly set, run the following command:
```sh
printenv fdtfile
```
7. Run the following command to resume the boot process of your Astrial:
```sh
boot
```
The selected DTB will be used until you change it again.