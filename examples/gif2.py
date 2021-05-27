
# Copyright (c) 2014 Adafruit Industries
# Author: Phil Howard, Tony DiCola
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
from PIL import Image
#new joystick screen
import time
import random
from colorsys import hsv_to_rgb
import board
from digitalio import DigitalInOut, Direction
from PIL import Image, ImageDraw, ImageFont



#import ST7789
import time
import sys
import adafruit_rgb_display.st7789 as st7789

print("""
gif.py - Display a gif on the LCD.

If you're using Breakout Garden, plug the 1.3" LCD (SPI)
breakout into the front slot.
""")

#if len(sys.argv) > 1:
#    image_file = sys.argv[1]
#else:
#    print("Usage: {} <filename.gif>".format(sys.argv[0]))
#    sys.exit(0)



# Create TFT LCD display class.
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

#from PIL import Image
from PIL import ImageSequence
with Image.open("deployrainbows.gif") as im:
    for frame in ImageSequence.Iterator(im):
        im.seek(1) # skip to the second frame

        try:
            while 1:
                im.seek(im.tell()+1)
            # do something to im
        except EOFError:
            pass # end of sequence

# Initialize display.
#disp.begin()

#width = disp.width
#height = disp.height

# Load an image.
#print('Loading gif: {}...'.format(image_file))
#image = Image.open(image_file)

#print('Drawing gif, press Ctrl+C to exit!')
#print(image.format, image.size, image.mode)
#image.convert('RGB')
#frame = 0



#while True:
#    try:
#        image = image.convert('RGB')
#        print(image.format, image.size, image.mode)
#        image.seek(frame)
#        disp.image(image.resize((width, height)))
#        frame += 1
#        time.sleep(0.05)

#    except EOFError:
#        frame = 0
