#All Code Copyrighted and patent pending to Snarflakes. 
#No unauthorized use of code allowed

import csv
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
from csv import reader

#construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="qrcodes.csv", help="path to output CSV file containing qrcode data")
args = vars(ap.parse_args())


#open the output CSV file for writing and initialize the set of qrcodes found thus far
csv2 = open(args["output"], "a")
found = set()

x = 0

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


#splash screen
image = Image.open('nftydaze3.jpg')
image = image.resize((WIDTH, HEIGHT))
# Draw the image on the display hardware.
print('Drawing Splash image')
disp.image(image)
time.sleep(3)

#### Add default most recently added NFT as base NFT displayed (can increase splash screen time)

opened_file = open('qrcodes.csv')
read_file = reader(opened_file)
apps_data = list(read_file)
x = (len(apps_data) - 1)
onelink = apps_data[x][1]

try:
    response = requests.get(onelink)

except HTTPError as e:
    print("can't connect to internet:HTTPError")
   #inform them of the specific error here (based off the error code)
except URLError as e:
    print("can't connect to internet:URLError")

    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    im = Image.new("RGB", (240, 240), "blue")
    d = ImageDraw.Draw(im)
    d.line(((0, 120), (200, 120)), "gray")
    d.line(((120, 0), (120, 200)), "gray")

    d.text((120, 80), "___(°)~(°)_________", fill="black", anchor="ms", font=font)
    d.text((120, 100), "User:    ", fill="black", anchor="rs", font=font)
    d.text((120, 120), "No internet connected", fill="black", anchor="ms", font=font)
    d.text((120, 140), "to fetch NFT images", fill="black", anchor="ms", font=font)
    d.text((120, 160), "Connect your phone", fill="black", anchor="ms", font=font)
    d.text((120, 180), "wifi to 'HomeBridge'", fill="black", anchor="ms", font=font)
    d.text((120, 200), "Iphone to Iphone Hotspots", fill="black", anchor="ms", font=font)
    d.text((120, 220), "don't work_______", fill="black", anchor="ms", font=font)

#       im = im.rotate()
    disp.image(im)

   #inform them of the specific error here
except Exception as e:
    print("can't connect to internet:Exception")
   #inform them that a general error has occurred 


image_bytes = io.BytesIO(response.content)
img = PIL.Image.open(image_bytes)
resized_img = img.resize((WIDTH, HEIGHT))
disp.image(resized_img)
time.sleep(0.25)



#original audio code

#button1=A=key1
button1 = digitalio.DigitalInOut(board.D21)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

#button2=Y=key2
button2 = digitalio.DigitalInOut(board.D20)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

#button3=X
#button3 = digitalio.DigitalInOut(board.D16)
#button3.direction = digitalio.Direction.INPUT
#button3.pull = digitalio.Pull.UP

#button4=B=key3
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



print("""
Pick your Gan Punk
""")

#index = 0


while True:
    if not button1.value:
        print("Shutting Down")

#Shutdown display screen Splash
        image = Image.open('nftydaze3.jpg')
        image = image.resize((WIDTH, HEIGHT))
        print('Drawing image')
        disp.image(image)

        time.sleep(5)
        os.system("sudo shutdown -h now")
        while 1:
            time.sleep(1)

#        subprocess.Popen(['omxplayer', '-o', 'alsa', mp3_files[0]])
#        time.sleep(0.25)

#        index += 1
#        if index >= len(mp3_files):
#            index = 0
#        print("--- " + mp3_files[index] + " ---")

    if not button2.value:
        print("Delete Your NFT")
        removenft = x + 1

#        lines = list()

        updatedlist=[]
#CSV starts as object, list? turns it into a string
        with open("qrcodes.csv",newline="") as f:
            print(type(f))
            read_file = reader(f)
            mylist = list(read_file)
            onelink = mylist[removenft][1]

#            print(type(mylist))
#            print(type(mylist[0][0]))
#            print(type(mylist[0][1]))
#            reader=csv.reader(f)
#            print(mylist)
            for row in mylist: #for every row in the file
                print(row)
                print(row[1])
                print(onelink)
#                print(type(row[1]))
#                print(row[1])
                if row[1]!=onelink: #as long as the username is not in the row .......
                    updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'
            print(updatedlist)
            print(updatedlist[0][1])
            print(type(updatedlist[0][1]))
            print(updatedlist[0][0])
            print(type(updatedlist[0][0]))
        with open("qrcodes.csv","w",newline="") as f:
            mywriter=csv.writer(f)
           
            for value in updatedlist:
                mywriter.writerow(value)
# Write.writerows([updatedlist])
            print("File has been updated")
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
            im = Image.new("RGB", (240, 240), "red")
            d = ImageDraw.Draw(im)
            d.line(((0, 120), (200, 120)), "gray")
            d.line(((120, 0), (120, 200)), "gray")

            d.text((120, 80), "   (°)~(°)_________", fill="black", anchor="ms", font=font)
            d.text((120, 100), "User:    ", fill="black", anchor="rs", font=font)
            d.text((120, 120), "Deleted NFT", fill="black", anchor="ms", font=font)
            d.text((120, 140), "They are gone", fill="black", anchor="ms", font=font)
            d.text((120, 160), "Not forever", fill="black", anchor="ms", font=font)
            d.text((120, 180), "Just", fill="black", anchor="ms", font=font)
            d.text((120, 200), "Reload", fill="black", anchor="ms", font=font)
            d.text((120, 220), "__________________", fill="black", anchor="ms", font=font)

#        im = im.rotate()
            disp.image(im)





#        subprocess.Popen(['omxplayer', '-o', 'alsa', mp3_files[1]])
#        print('--- Playing ' + mp3_files[index] + ' ---')
#        print('--- Press button 3(X) to clear playing mp3s. ---')
        time.sleep(0.25)

    if not button4.value:
#SlideShow Mode
        print("SlideShow Mode")
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        im = Image.new("RGB", (240, 240), "pink")
        d = ImageDraw.Draw(im)
        d.line(((0, 120), (200, 120)), "gray")
        d.line(((120, 0), (120, 200)), "gray")

        d.text((120, 80), "   (°)~(°)_________", fill="black", anchor="ms", font=font)
#        d.text((120, 100), "User:    ", fill="black", anchor="rs", font=font)
        d.text((120, 120), "SlideShow", fill="black", anchor="ms", font=font)
        d.text((120, 140), "Mode", fill="black", anchor="ms", font=font)
        d.text((120, 160), "Activated", fill="black", anchor="ms", font=font)
#        d.text((120, 180), "when captured. Repeat.", fill="black", anchor="ms", font=font)
#        d.text((120, 200), "Press Down when done!", fill="black", anchor="ms", font=font)
#        d.text((120, 220), "__________________", fill="black", anchor="ms", font=font)

#        im = im.rotate()
        disp.image(im)

        for value in apps_data:
             print(value[1])
             onelink = value[1]
             response = requests.get(onelink)
             image_bytes = io.BytesIO(response.content)
             img = PIL.Image.open(image_bytes)
             resized_img = img.resize((WIDTH, HEIGHT))
             disp.image(resized_img)
             time.sleep(5)
             #how to stop loop? if any other button is pressed?

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
#Aim at QR codes; new NFT will flash when captured:  display screen Splash

        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        im = Image.new("RGB", (240, 240), "blue")
        d = ImageDraw.Draw(im)
        d.line(((0, 120), (200, 120)), "gray")
        d.line(((120, 0), (120, 200)), "gray")

        d.text((120, 80), "___(°)~(°)_________", fill="black", anchor="ms", font=font)
        d.text((120, 100), "User:    ", fill="black", anchor="rs", font=font)
        d.text((120, 120), "Aim 12 inches away", fill="black", anchor="ms", font=font)
        d.text((120, 140), "from QR Codes", fill="black", anchor="ms", font=font)
        d.text((120, 160), "New NFT will flash", fill="black", anchor="ms", font=font)
        d.text((120, 180), "when captured. Repeat.", fill="black", anchor="ms", font=font)
        d.text((120, 200), "Press Down when done!", fill="black", anchor="ms", font=font)
        d.text((120, 220), "__________________", fill="black", anchor="ms", font=font)

#        im = im.rotate()
        disp.image(im)


#Start QRcode capture

        cap = cv2.VideoCapture(-1)
        font = cv2.FONT_HERSHEY_PLAIN

        while True:
            _, frame = cap.read()

            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                print("Data", obj.data)
                print(type(obj.data))
#Display on screen confirmation of reading
                cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                            (255, 0, 0), 3)
                #convertbytes object data to string
                qrcodeData = obj.data.decode("utf-8")
#Flash NFT to signal capture
                response = requests.get(qrcodeData)
                image_bytes = io.BytesIO(response.content)
                img = PIL.Image.open(image_bytes)
                resized_img = img.resize((WIDTH, HEIGHT))
                disp.image(resized_img)
                time.sleep(0.50)
#Go black
                print("QRCode scanned to Display Screen")
#	clear screen to black ********Add Saved in Ascii? "press joystick down to stop scanning QRcodes?"
#                disp.begin()
                img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
                draw = ImageDraw.Draw(img)
                disp.image(img)
                time.sleep(0.25)
## Add except if trying to scan  marketplace, not pure image data 
## Add except if no qrcode was scanned

                #if qrcode text is currently not in our csv file, write timestampe and
                #qrcode to disk and update the set
                if qrcodeData not in found:
                    csv2.write("{},{}\n".format(datetime.datetime.now(), qrcodeData))
                    csv2.flush()
                    found.add(qrcodeData)
            if not button_R.value:

#To do: Splash: ALL Stored:  Resume Selecting Your NFT to display
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
                im = Image.new("RGB", (240, 240), "yellow")
                d = ImageDraw.Draw(im)
                d.line(((0, 120), (200, 120)), "gray")
                d.line(((120, 0), (120, 200)), "gray")

                d.text((120, 80), "___(°)~(°)_________", fill="black", anchor="ms", font=font)
                d.text((120, 100), "User:    ", fill="black", anchor="rs", font=font)
                d.text((120, 120), "All QRCodes Stored!", fill="black", anchor="ms", font=font)
                d.text((120, 140), "Press Left or", fill="black", anchor="ms", font=font)
                d.text((120, 160), "Right to select", fill="black", anchor="ms", font=font)
                d.text((120, 180), "your preferred NFT", fill="black", anchor="ms", font=font)
                d.text((120, 200), "to be displayed", fill="black", anchor="ms", font=font)
                d.text((120, 220), "__________________", fill="black", anchor="ms", font=font)
#    im = im.rotate(180)
                disp.image(im)

#set carousel at newest added nft
                opened_file = open('qrcodes.csv')
                read_file = reader(opened_file)
                apps_data = list(read_file)
                x = (len(apps_data) - 1)
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
        opened_file = open('qrcodes.csv')
        read_file = reader(opened_file)
        apps_data = list(read_file)
        onelink = apps_data[x][1]
        x += 1
        print(len(apps_data))
        if x > (len(apps_data) - 1):
            x = 0

#display next NFT in order of CSV
        response = requests.get(onelink)
        image_bytes = io.BytesIO(response.content)
        img = PIL.Image.open(image_bytes)
        resized_img = img.resize((WIDTH, HEIGHT))
        disp.image(resized_img)
        time.sleep(0.25)


    if not button_U.value:
#reverse direction scrolling
        print("Your Saved Gan Punks:reverse direction")
        opened_file = open('qrcodes.csv')
        from csv import reader
        read_file = reader(opened_file)
        apps_data = list(read_file)
        nftlinks = []
        onelink = apps_data[x][1]
        x -= 1
        print(len(apps_data))
        if x < 0:
            x = (len(apps_data) - 1)

#display next NFT in reverse order of CSV
        response = requests.get(onelink)
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






