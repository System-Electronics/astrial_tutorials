# Tutorial 05 - USB Camera
## Material required
* 1 x Astrial
* 1 x CM4 carrier
* 1 x USB Camera Innodisk EV2U-SGR1

## Setup
### Hardware setup
Connect the USB camera to the CM4's USB port.
Also, for this tutorial, you need to connect a display to the Astrial's HDMI port, in order to see the video stream.

![Photo](images/photo.jpg)

### Copy the example script
Copy the `detection.sh` script to the Astrial, under the `/home/root/apps/detection` folder. This script uses the USB camera to detect objects and display the video stream on the screen.

```sh
scp detection.sh root@<astrial_ip>:/home/root/apps/detection
```

### Check the camera's input resolution
Your camera may have different resolutions available. To check the available resolutions, and read the device id, you can use the `gst-device-monitor-1.0` command:
```sh
gst-device-monitor-1.0
```

The output will show the available resolutions for the camera and the device id, like this:
```
Device found:

	name  : Innodisk USB Camera: Innodisk U
	class : Video/Source
	caps  : video/x-raw, format=YUY2, width=1920, height=1080, pixel-aspect-ratio=1/1, framerate=5/1
--------->  image/jpeg, width=1920, height=1080, pixel-aspect-ratio=1/1, framerate=30/1
	        image/jpeg, width=1280, height=720, pixel-aspect-ratio=1/1, framerate=30/1
	        image/jpeg, width=640, height=480, pixel-aspect-ratio=1/1, framerate=30/1
	properties:
		udev-probed = true
		device.bus_path = platform-xhci-hcd.1.auto-usb-0:1.1:1.0
		sysfs.path = /sys/devices/platform/soc@0/32f10100.usb/38100000.usb/xhci-hcd.1.auto/usb1/1-1/1-1.1/1-1.1:1.0/video4linux/video3
		device.bus = usb
		device.subsystem = video4linux
		device.vendor.id = 196d
		device.vendor.name = Innodisk\x20Technology\x20Co.\x2c\x20Ltd.
		device.product.id = b202
		device.product.name = Innodisk USB Camera: Innodisk U
		device.serial = Innodisk_Technology_Co.__Ltd._Innodisk_USB_Camera_Y2400B7E4_1713865854
		device.capabilities = :capture:
		device.api = v4l2
------> device.path = /dev/video3
		v4l2.device.driver = uvcvideo
		v4l2.device.card = Innodisk USB Camera: Innodisk U
		v4l2.device.bus_info = usb-xhci-hcd.1.auto-1.1
		v4l2.device.version = 331591 (0x00050f47)
		v4l2.device.capabilities = 2225078273 (0x84a00001)
		v4l2.device.device_caps = 69206017 (0x04200001)
	gst-launch-1.0 v4l2src device=/dev/video3 ! ...
```

### Run the script
Run the script:
```sh
cd /home/root/apps/detection
./detection.sh -i /dev/video3 -w 1920 -h 1080
```

Make sure to replace `/dev/video3` with the device id of your camera, and the width and height with the desired resolution.
