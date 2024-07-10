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

## Use a custom DTB
In some tutorials, we use a custom Device Tree (DTS) to enable specific functionalities. To use a custom DTS, replace the default Device Tree Blob (DTB) with the one provided in the `resources` directory of that tutorial: insert the SD card in your PC and replace the .dtb file you find in the `boot` partition with the new one.