import os
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

#qr code modules
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import argparse
import datetime
import imutils

#construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="qrcodes.csv", help="path to output CSV file containing qrcode data")
args = vars(ap.parse_args())


#open the output CSV file for writing and initialize the set of qrcodes found thus far
csv = open(args["output"], "a")
found = set()



# set up camera object
#cap = cv2.VideoCapture(-1)

# QR code detection object
#detector = cv2.QRCodeDetector()


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
button_R.pull = digitalio.Pull.UP

button_U = DigitalInOut(board.D6)
button_U.direction = Direction.INPUT
button_U.pull = digitalio.Pull.UP

button_D = DigitalInOut(board.D19)
button_D.direction = Direction.INPUT
button_D.pull = digitalio.Pull.UP

button_C = DigitalInOut(board.D13)
button_C.direction = Direction.INPUT
button_C.pull = digitalio.Pull.UP


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
        print("Shutting Down")
        time.sleep(5)
        os.system("sudo shutdown -h now")
        while 1:
            time.sleep(1)
#        print("Your First Gan Punk")
#        response = requests.get("https://lh3.googleusercontent.com/ObAoTdEUzmtVFWdLoTOoqrjCkBpOP35n83PoIGhFXWF2Ys1DkWq4SN9kRlIUdvJ9nCHGbD3nQr2GivpoF4exNR017yycYAsf3WkW5Q=s0")
#        image_bytes = io.BytesIO(response.content)
#        img = PIL.Image.open(image_bytes)
#        resized_img = img.resize((WIDTH, HEIGHT))
#        disp.image(resized_img)

#        subprocess.Popen(['omxplayer', '-o', 'alsa', mp3_files[0]])
#        time.sleep(0.25)

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
        time.sleep(0.25)

    if not button_C.value:
        print("Your QR Gan Punk")
        cap = cv2.VideoCapture(-1)
        font = cv2.FONT_HERSHEY_PLAIN

        while True:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                print("Data", obj.data)
                print(type(obj.data))
                cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                            (255, 0, 0), 3)
                #convertbytes object data to string
                qrcodeData = obj.data.decode("utf-8")
                #if qrcode text is currently not in our csv file, write timestampe and
                #qrcode to disk and update the set
                if qrcodeData not in found:
                    csv.write("{},{}\n".format(datetime.datetime.now(), qrcodeData))
                    csv.flush()
                    found.add(qrcodeData)
            if not button_R.value:
                print("Saved your punk")
                break
#                    qrcodedata = obj.data
#                    punknew = qrcodedata.decode("utf-8")

                    #punknew = qrcodedata
                    #free camera object and exit
        cap.release()
        cv2.destroyAllWindows()
        print(qrcodeData)

    if not button_D.value:
        print("Your Saved Gan Punks")
#        for value in qrcodeData[1]:
        
        response = requests.get(qrcodeData)
        image_bytes = io.BytesIO(response.content)
        img = PIL.Image.open(image_bytes)
        resized_img = img.resize((WIDTH, HEIGHT))
        disp.image(resized_img)
        time.sleep(0.25)


#        time.sleep(0.25)
#        while True:
            # get the image
#            _, img = cap.read()
            # get bounding box coords and data
#            data, bbox, _ = detector.detectAndDecode(img)

            # if there is a bounding box, draw one, along with the data
#            if(bbox is not None):
#                for i in range(len(bbox)):
#                     cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 255), thickness=2)
#                cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
#                if data:
#                    print("data found: ", data)
            # display the image preview
#            cv2.imshow("code detector", img)
#            if(cv2.waitKey(1) == ord("q")):
#                break
        # free camera object and exit
#        cap.release()
#        cv2.destroyAllWindows()


#        response = requests.get("https://lh3.googleusercontent.com/zpZj6rX-zlK7qTvqyDpMUdZy3HHjY1t1QpjQ6mXglYt3pZig1ACkQeA7hW8nyzwQpFA5QCDzHdd61Xy2xKZuvc_bQCfjmTFphUzc=s0") 
#        image_bytes = io.BytesIO(response.content)
#        img = PIL.Image.open(image_bytes)
#        resized_img = img.resize((WIDTH, HEIGHT))
#        disp.image(resized_img)





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
