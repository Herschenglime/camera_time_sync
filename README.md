# Timing Testing

This repo contains basic testing and docs for using the external trigger feature on our usb cam. It follows the arducam docs:
https://www.arducam.com/100fps-global-shutter-color-usb-camera-board-1mp-ov9782-uvc-webcam-module-with-low-distortion-m12-lens-without-microphones-for-computer-laptop-android-device-and-raspberry-pi-arducam.html

Wonderfully, NVidia made the GPIO pins input-only, which is no good for our external triggering pins. I followed this guide to fix that:
https://jetsonhacks.com/2025/04/07/device-tree-overlays-on-jetson-scary-but-fun/

Here's the linked repo with the fix:
https://github.com/jetsonhacks/jetson-orin-gpio-patch