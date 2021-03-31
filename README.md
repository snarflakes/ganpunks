# Python ST7789 with GanPunks Program

[![Build Status](https://travis-ci.com/pimoroni/st7789-python.svg?branch=master)](https://travis-ci.com/pimoroni/st7789-python)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/st7789-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/st7789-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/st7789.svg)](https://pypi.python.org/pypi/st7789)
[![Python Versions](https://img.shields.io/pypi/pyversions/st7789.svg)](https://pypi.python.org/pypi/st7789)


GAN Punks: these instructions include the proper library to run your Pirate Audio Display and the NFT viewer/audio program to view and hear your NFTs.

screen (also available at adafruit) - https://shop.pimoroni.com/products/pirate-audio-mini-speaker
raspberrypi 0 -wh - https://www.adafruit.com/product/3708
microSD card- https://www.amazon.com/Samsung-Endurance-32GB-Micro-Adapter/dp/B07B98GXQT
slim battery pack (optional) - https://www.aliexpress.com/item/32954180664.html?spm=a2g0s.12269583.0.0.38da1736QdV4CH

Python library to control an ST7789 TFT LCD display

Designed specifically to work with a ST7789 based 240x240 pixel TFT SPI display. (Specifically the [1.3" SPI LCD from Pimoroni](https://shop.pimoroni.com/products/1-3-spi-colour-lcd-240x240-breakout)).

![myImage](https://pbs.twimg.com/media/Exwskm7UYAUF7Cz?format=jpg&name=4096x4096)


# Installation

Basic Raspberry Pi Zero setup for NOOBS.  start here if you have no clue what to do with your hardware.
https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html

after above completed steps proceed below. 

Make sure you have the following dependencies (modules):

````
sudo apt-get update
sudo apt-get install python-rpi.gpio python-spidev python-pip python-pil python-numpy
````

Install this library by running:

````
sudo pip install st7789
````

Prerequisites
(These instructions assume that your Raspberry Pi is already connected to the Internet, happily running pip and has Python3 installed)

If you are running the Pi headless, connect to your Raspberry Pi using ssh.


Install & Run
Copy the files from this repository onto the Pi, or clone using:

```````````
cd ~
git clone https://github.com/snarflakes/ganpunks.git
cd ganpunks
```````````

Run the script using:

`````````````
python3 image.py
`````````````





# How to Adapt program for your own Gan Punk NFTs:

Navigate to raspberry pi ganpunks directory

```````````
sudo nano image.py
```````````

Buttons are 1=A, 2=Y, 3=X, 4=B in the code

Scroll down till you reach the below code in grey:
replace https:// address with your address in code for each button1,button2,button3,button4
I left button3 "X" as a pure back background button to avoid screen burn in.

Precaution: use the proper web link:
click the image of your NFT, then from new image box: 
right click your Bastard NFT: 
click COPY IMAGE ADDRESS 
use that link and replace the existing opensea (googleusercontent.com) link below for each button

``````````
while True:
    if not button1.value:
        print("Your First Gan Punk")
****    response = requests.get("https://lh3.googleusercontent.com/ObAoTdEUzmtV$....
        image_bytes = io.BytesIO(response.content)
        img = PIL.Image.open(image_bytes)
        resized_img = img.resize((WIDTH, HEIGHT))
        disp.display(resized_img)

``````````


To include audio tracks: you need to upload them into the raspberry PI zero from a USB stick (pi/media/) then copy and paste each audio file into the main GanPUNK application directory.  
.mp3 or .m4a should work.
delete existing .mp3 and .m4a to ensure only your mp3s get played.  you might have to change the order of your gan punks to match your desired music order.  I don't know how to re-sort audio files on the pi.  I only have music attached to button A and button Y.  Just add in the two lines of code (space bar indented) under the other buttons that don't have the below two lines if you want sounds matched to all buttons.

``````
   subprocess.Popen(['omxplayer', '-o', 'alsa', mp3_files[1]])
   time.sleep(0.25)
``````







# Licensing & History

This library is a modification of a modification of code originally written by Tony DiCola for Adafruit Industries, and modified to work with the ST7735 by Clement Skau.

To create this ST7789 driver, it has been hard-forked from st7735-python which was originally modified by Pimoroni to include support for their 160x80 SPI LCD breakout.

## Modifications include:

* PIL/Pillow has been removed from the underlying display driver to separate concerns- you should create your own PIL image and display it using `display(image)`
* `width`, `height`, `rotation`, `invert`, `offset_left` and `offset_top` parameters can be passed into `__init__` for alternate displays
* `Adafruit_GPIO` has been replaced with `RPi.GPIO` and `spidev` to closely align with our other software (IE: Raspberry Pi only)
* Test fixtures have been added to keep this library stable

Pimoroni invests time and resources forking and modifying this open source code, please support Pimoroni and open-source software by purchasing products from us, too!

Adafruit invests time and resources providing this open source code, please support Adafruit and open-source hardware by purchasing products from Adafruit!

Modified from 'Modified from 'Adafruit Python ILI9341' written by Tony DiCola for Adafruit Industries.' written by Clement Skau.

MIT license, all text above must be included in any redistribution
