# Python ST7789 with GanPunks Program

[![Build Status](https://travis-ci.com/pimoroni/st7789-python.svg?branch=master)](https://travis-ci.com/pimoroni/st7789-python)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/st7789-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/st7789-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/st7789.svg)](https://pypi.python.org/pypi/st7789)
[![Python Versions](https://img.shields.io/pypi/pyversions/st7789.svg)](https://pypi.python.org/pypi/st7789)

GAN Punks: these instructions include the proper library to run your Pirate Audio Display and the NFT viewer/audio program to view and hear your NFTs.

Python library to control an ST7789 TFT LCD display

Designed specifically to work with a ST7789 based 240x240 pixel TFT SPI display. (Specifically the [1.3" SPI LCD from Pimoroni](https://shop.pimoroni.com/products/1-3-spi-colour-lcd-240x240-breakout)).

![myImage](https://pbs.twimg.com/media/Exwskm7UYAUF7Cz?format=jpg&name=4096x4096)


# Installation

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



Adapt program for your own Gan Punk NFTs:
Navigate to raspberry pi ganpunks directory

```````````
sudo nano image.py
```````````

Navigate to Buttons 1, 2, 3, 4 in the code
``````````
says this
``````````

Cut and paste the image links from opensea under each button
I left button "X" as a pure back background button to avoid screen burn in.

for example:
click the image of your NFT then in new image box: 
right click your Bastard NFT: 
click COPY IMAGE ADDRESS 
use that link and replace the existing opensea link for each button

To include audio tracks: you need to upload them into the raspberry PI zero from a USB stick then copy and paste each audio file into the main GanPUNK directory.  
.mp3 or .m4a should work.








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
