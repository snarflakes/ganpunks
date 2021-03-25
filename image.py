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

import ST7789 as ST7789

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
disp = ST7789.ST7789(
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
    dc=9,
    backlight=19,               # 18 for back BG slot, 19 for front BG slot.
    spi_speed_hz=80 * 1000 * 1000
)

WIDTH = disp.width
HEIGHT = disp.height


disp.begin()


#clear screen to black
#img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
#draw = ImageDraw.Draw(img)
#disp.display(img)

#punks

response = requests.get("https://lh3.googleusercontent.com/ObAoTdEUzmtVFWdLoTOoqrjCkBpOP35n83PoIGhFXWF2Ys1DkWq4SN9kRlIUdvJ9nCHGbD3nQr2GivpoF4exNR017yycYAsf3WkW5Q=s0")
image_bytes = io.BytesIO(response.content)
img = PIL.Image.open(image_bytes)

resized_img = img.resize((WIDTH, HEIGHT))

disp.display(resized_img)























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
