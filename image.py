# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
import logging
import requests
import io
import PIL

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#import ST7789 as ST7789

#audio button code
import time
from os import listdir
import subprocess
import board
import digitalio

#new joystick screen
import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789


print("""
image.py - Display an image on the LCD.

If you're using Breakout Garden, plug the 1.3" LCD (SPI)
breakout into the front slot.
""")

#if len(sys.argv) < 2:
#    print("Usage: {} <image_file>".format(sys.argv[0]))
#    sys.exit(1)

#image_file = sys.argv[1]

# Create ST7789 LCD display class.
#disp = ST7789.ST7789(
#    port=0,
#    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
#    dc=9,
#    backlight=19,               # 18 for back BG slot, 19 for front BG slot.
#    spi_speed_hz=80 * 1000 * 1000
#)

# Create the joystick display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D27)
BAUDRATE = 24000000
 
spi = board.SPI()
disp = st7789.ST7789(
    spi,
    height=240,
    y_offset=80,
    rotation=180,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

# Turn on the Backlight, can also use to turn off the backlight for power saving
backlight = DigitalInOut(board.D24)
backlight.switch_to_output()
backlight.value = True


WIDTH = disp.width
HEIGHT = disp.height


#disp.begin()

#original audio code

#button1=A
button1 = digitalio.DigitalInOut(board.D21)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

#button2=Y
button2 = digitalio.DigitalInOut(board.D20)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

#button3=X
#button3 = digitalio.DigitalInOut(board.D16)
#button3.direction = digitalio.Direction.INPUT
#button3.pull = digitalio.Pull.UP

#button4=B
button4 = digitalio.DigitalInOut(board.D16)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.UP

#direction pad
button_L = DigitalInOut(board.D5)
button_L.direction = Direction.INPUT
button_L.pull = digitalio.Pull.UP


button_R = DigitalInOut(board.D26)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D6)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D19)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D13)
button_C.direction = Direction.INPUT



#clear screen to black
#img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
#draw = ImageDraw.Draw(img)
#disp.display(img)

#punks





mp3_files = [ f for f in listdir('.') if f[-4:] == '.mp3' ] + [f for f in listdir('.') if f[-4:] == '.m4a' ]

if not len(mp3_files) > 0:
    print("No mp3 files found!")

print('--- Available mp3 files ---')
print(mp3_files)
#print('--- Press button 1(A) to select mp3, button 2(Y) to play current. ---')

print("""
Pick your Gan Punk
""")

#index = 0

while True:
    if not button1.value:
#	print("Your First Gan Punk")
        response = requests.get("https://lh3.googleusercontent.com/ObAoTdEUzmtVFWdLoTOoqrjCkBpOP35n83PoIGhFXWF2Ys1DkWq4SN9kRlIUdvJ9nCHGbD3nQr2GivpoF4exNR017yycYAsf3WkW5Q=s0")
        image_bytes = io.BytesIO(response.content)
        img = PIL.Image.open(image_bytes)
        resized_img = img.resize((WIDTH, HEIGHT))
        disp.image(resized_img)

#        subprocess.Popen(['omxplayer', '-o', 'alsa', mp3_files[0]])
        time.sleep(0.25)

#        index += 1
#        if index >= len(mp3_files):
#            index = 0
#        print("--- " + mp3_files[index] + " ---")

    if not button2.value:
        print("Your Second Gan Punk")
        response = requests.get("https://lh3.googleusercontent.com/DYojMNXtoKs5qyMncS8iWeL5nTM100jL1o0WY-BSO6sXKIWAH9OYph-TyvhhP84lkwzR0XvjnKn_pQrMI_HxXtqs82VjmhygTr-6xZM=s0")
        image_bytes = io.BytesIO(response.content)
        img = PIL.Image.open(image_bytes)
        resized_img = img.resize((WIDTH, HEIGHT))
        disp.image(resized_img)

#        subprocess.Popen(['omxplayer', '-o', 'alsa', mp3_files[1]])
#        print('--- Playing ' + mp3_files[index] + ' ---')
#        print('--- Press button 3(X) to clear playing mp3s. ---')
        time.sleep(0.25)

#    if not button3.value:
#        print("Clear Screen")
#	clear screen to black
#        img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
#        draw = ImageDraw.Draw(img)
#        disp.display(img)
#        time.sleep(0.25)

    if not button4.value:
        print("Your Third Gan Punk")
        response = requests.get("https://lh3.googleusercontent.com/lyiX1hFcQGcSPq1Fjmd28_89Q93q-QoJdLZ2iEgyqTmuQarXlKb2E5AjiH4fLdCGxxgYN9BuwDh3wugS4jTmhp2mFcQ6ewdFkgiz6Q=s0")
        image_bytes = io.BytesIO(response.content)
        img = PIL.Image.open(image_bytes)
        resized_img = img.resize((WIDTH, HEIGHT))
        disp.image(resized_img)


    if not button_L.value:
        print("Your fourth Gan Punk")
        response = requests.get("https://lh3.googleusercontent.com/zpZj6rX-zlK7qTvqyDpMUdZy3HHjY1t1QpjQ6mXglYt3pZig1ACkQeA7hW8nyzwQpFA5QCDzHdd61Xy2xKZuvc_bQCfjmTFphUzc=s0") 
        image_bytes = io.BytesIO(response.content)
        img = PIL.Image.open(image_bytes)
        resized_img = img.resize((WIDTH, HEIGHT))
        disp.image(resized_img)


#punks

#response = requests.get("https://lh3.googleusercontent.com/ObAoTdEUzmtVFWdLoTOoqrjCkBpOP35n83PoIGhFXWF2Ys1DkWq4SN9kRlIUdvJ9nCHGbD3nQr2GivpoF4exNR017yycYAsf3WkW5Q=s0")
#image_bytes = io.BytesIO(response.content)
#img = PIL.Image.open(image_bytes)

#resized_img = img.resize((WIDTH, HEIGHT))

#disp.display(resized_img)























# Initialize display.
#disp.begin()

# Load an image.
#print('Loading image: {}...'.format(img))
#img = Image.open(img)

# Resize the image
#img = Image.resize((WIDTH, HEIGHT))

# Draw the image on the display hardware.
print('Drawing image')

#disp.display(img)
