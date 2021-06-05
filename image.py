#All Code Copyrighted and patent pending to Snarflakes. 
#No unauthorized use of code allowed

import csv
import os
import sys
import logging
import requests
import io
import PIL
from signal import pause
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#import ST7789 as ST7789

#audio button code
import subprocess
import board
from gpiozero import Button

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

#check internet
import socket

#menu threading
#import threading
#from threading import Thread

#def do_somethingstop():
    
#    if not button1.value:
#    if not button2.value:
#        break
#    for _ in range(sys.maxsize**10):
#        if not button3.value:
#            switch = True
#            t1.stop()
#            t2.stop()
#            print("button3")
#            break

#def do_something():
#    for value in apps_data:
#        print(value[1])
#        onelink = value[1]
#        response = requests.get(onelink)
#        image_bytes = io.BytesIO(response.content)
#        img = PIL.Image.open(image_bytes)
#        resized_img = img.resize((WIDTH, HEIGHT))
#        disp.image(resized_img)
#        time.sleep(5)
#        if t2.isAlive() != True:
#            break


#construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="qrcodes.csv", help="path to output CSV file containing qrcode data")
args = vars(ap.parse_args())


#open the output CSV file for writing and initialize the set of qrcodes found thus far
csv2 = open(args["output"], "a")
found = set()

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

print("""
image.py - Display an image on the LCD.

""")

#splash screen
image = Image.open('nftydaze3.jpg')
image = image.resize((WIDTH, HEIGHT))
# Draw the image on the display hardware.
print('Drawing Splash image')
disp.image(image)
time.sleep(6)

# Added default most recently added NFT as base NFT displayed (can increase splash screen time)

opened_file = open('qrcodes.csv')
read_file = reader(opened_file)
apps_data = list(read_file)
x = (len(apps_data) - 1)
onelink = apps_data[x][1]

#check internet connection
try:
    response = requests.get(onelink)

except Exception:
    print("can't connect to internet:socket gaierror")

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
    d.text((120, 220), "don't work:shutting down in 2mins", fill="black", anchor="ms", font=font)

#       im = im.rotate()
    disp.image(im)
    time.sleep(120)

    print("Re-Connect:Auto Shutting Down in 2 minutes")

    try:
        response = requests.get(onelink)

    except Exception:
        print("retry connect internet:can't connect to internet:socket gaierror")

        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        im = Image.new("RGB", (240, 240), "red")
        d = ImageDraw.Draw(im)
        d.line(((0, 120), (200, 120)), "gray")
        d.line(((120, 0), (120, 200)), "gray")

        d.text((120, 80), "___(°)~(°)_________", fill="black", anchor="ms", font=font)
        d.text((120, 100), "User:    ", fill="black", anchor="rs", font=font)
        d.text((120, 120), "Retried internet, Still", fill="black", anchor="ms", font=font)
        d.text((120, 140), "No internet connected", fill="black", anchor="ms", font=font)
        d.text((120, 160), "Shutting Down", fill="black", anchor="ms", font=font)
        d.text((120, 180), "now!", fill="black", anchor="ms", font=font)
#        d.text((120, 200), "fasfd", fill="black", anchor="ms", font=font)
#        d.text((120, 220), "n in 2mins", fill="black", anchor="ms", font=font)

#       im = im.rotate()
        disp.image(im)
        time.sleep(30)


        #Shutdown display screen Splash
        image = Image.open('nftydaze3.jpg')
        image = image.resize((WIDTH, HEIGHT))
        print('Drawing image')
        disp.image(image)

        time.sleep(5)
        os.system("sudo shutdown -h now")
        while 1:
            time.sleep(1)
    
image_bytes = io.BytesIO(response.content)
#check for bad link
try:
    img = PIL.Image.open(image_bytes)
    resized_img = img.resize((WIDTH, HEIGHT))
    disp.image(resized_img)
    time.sleep(0.25)            
except PIL.UnidentifiedImageError:
    print("Bad Link/File")


def internet(host="8.8.8.8", port=53, timeout=3):
	"""
	Host: 8.8.8.8 (google-public-dns-a.google.com)
	OpenPort: 53/tcp
	Service: domain (DNS/TCP)
	"""
	try:
		socket.setdefaulttimeout(timeout)
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True
	except socket.error as ex:
		print(ex)
		return False

def shut_down():
    print("Shutting Down")
    image = Image.open('nftydaze3.jpg')
    image = image.resize((WIDTH, HEIGHT))
    print('Drawing image')
    disp.image(image)

    time.sleep(5)
    os.system("sudo shutdown -h now")
    while 1:
        time.sleep(1)

def delete_NFT():
    global x
    global apps_data
    print("Delete Your NFT")
#works when setting up minus 1 scrolling, can you say if last button press was up? and if last button press was down? then you can make a logic decision for removenft. also last nft
#in data base cannot be removed because of cycling action setting up going back to top. not correct with down button (left) removal.
    removenft = x 
    updatedlist=[]

    with open("qrcodes.csv",newline="") as f:
        print(type(f))
        read_file = reader(f)
        mylist = list(read_file)
        print(removenft)
        onelink = mylist[removenft][1]
        print(onelink)
#            x = x - 1
#            print(type(mylist))
#            print(type(mylist[0][0]))
#            print(type(mylist[0][1]))
#            reader=csv.reader(f)
#            print(mylist)
        for row in mylist: #for every row in the file
#                print(row)
#                print(row[1])
#                print(onelink)
#                print(type(row[1]))
#                print(row[1])
            if row[1]!=onelink: #as long as the username is not in the row .......
                updatedlist.append(row) #add each row, line by line, into a list called 'udpatedlist'
        print(updatedlist)
#            print(updatedlist[0][1])
#            print(type(updatedlist[0][1]))
    with open("qrcodes.csv","w",newline="") as f:
        mywriter=csv.writer(f)
           
        for value in updatedlist:
            mywriter.writerow(value)
# Write.writerows([updatedlist])
        print("File has been updated")
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        im = Image.new("RGB", (240, 240), "red")
        d = ImageDraw.Draw(im)
#            d.line(((0, 120), (200, 120)), "gray")
#            d.line(((120, 0), (120, 200)), "gray")

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
    if x == 0:
        print("1st nft deleted; restart list")
        x = (len(apps_data) - 1) 
        
    time.sleep(0.25)

#slideshow_on = False
def slideshow_mode():
#    global slideshow_on

    global apps_data
    print("SlideShow Mode")
#    if slideshow_on:
    if internet():
        
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 30)
        im = Image.new("RGB", (240, 240), "pink")
        d = ImageDraw.Draw(im)
#        d.line(((0, 120), (200, 120)), "gray")
#        d.line(((120, 0), (120, 200)), "gray")

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

#        for i in range(sys.maxsize**10): 
#        switch = False
#        for _ in range(sys.maxsize**10):
#            t1 = threading.Thread(target=do_something)
#            t2 = threading.Thread(target=do_somethingstop)
#            t2.start()
#            t1.start()

#            t1.join()
#            t2.join()
        for _ in range(3):
            for value in apps_data:
#            t1.start()
#            t2.start()
                print(value[1])
                onelink = value[1]
                response = requests.get(onelink)
                image_bytes = io.BytesIO(response.content)
#scan for corrupted link
                try:
                    img = PIL.Image.open(image_bytes)
                    resized_img = img.resize((WIDTH, HEIGHT))
                    disp.image(resized_img)
                    time.sleep(5)            
                except PIL.UnidentifiedImageError:
                    print("Bad Link/File")
               
            
            time.sleep(0.25)
        time.sleep(0.25)
    else:
        print("no internet available")

# slideshow_on = not slideshow_on
#                b.start()

#            if not button_D.value:
#                print("stop slideshow")
#                a.stop()
#                break

 
             #how to stop loop? if any other button is pressed?

def special_NFT():
    print("Your fourth Gan Punk")
    response = requests.get("https://lh3.googleusercontent.com/zpZj6rX-zlK7qTvqyDpMUdZy3HHjY1t1QpjQ6mXglYt3pZig1ACkQeA7hW8nyzwQpFA5QCDzHdd61Xy2xKZuvc_bQCfjmTFphUzc=s0")
    image_bytes = io.BytesIO(response.content)
    img = PIL.Image.open(image_bytes)
    resized_img = img.resize((WIDTH, HEIGHT))
    disp.image(resized_img)
    time.sleep(0.25)

camera_on = False

def qr_capture():
    global apps_data
    global x
    global camera_on
#    cap = cv2.VideoCapture(-1)

    print("Your QR Gan Punk")
#Aim at QR codes; new NFT will flash when captured:  display screen Splash
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    im = Image.new("RGB", (240, 240), "blue")
    d = ImageDraw.Draw(im)
#        d.line(((0, 120), (200, 120)), "gray")
#        d.line(((120, 0), (120, 200)), "gray")

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
#display on screen flash confirmation of reading
            img = Image.new('RGB', (WIDTH, HEIGHT), color=(255, 255, 255))
            draw = ImageDraw.Draw(img)
            disp.image(img)
            time.sleep(0.25)

            img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
            draw = ImageDraw.Draw(img)
            disp.image(img)
            time.sleep(0.25)

#            cv2.putText(frame, str(obj.data), (50, 50), font, 2,
#                        (255, 0, 0), 3)
#convertbytes object data to string
            qrcodeData = obj.data.decode("utf-8")
#flash NFT to signal capture, 
#first go black/stop scanning/process
            response = requests.get(qrcodeData)
            image_bytes = io.BytesIO(response.content)

#check for mp4 image file
            try:
                img = PIL.Image.open(image_bytes)
            except PIL.UnidentifiedImageError:
                print("MPEG scan attempted")
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
                im = Image.new("RGB", (240, 240), "red")
                d = ImageDraw.Draw(im)
#        d.line(((0, 120), (200, 120)), "gray")
#        d.line(((120, 0), (120, 200)), "gray")
                d.text((120, 80), "___(°)~(°)_________", fill="black", anchor="ms", font=font)
                d.text((120, 100), "DON'T do that", fill="black", anchor="rs", font=font)
                d.text((120, 120), "NO MPEGS/VIDEOS", fill="black", anchor="ms", font=font)
                d.text((120, 140), "on this model", fill="black", anchor="ms", font=font)
                d.text((120, 160), "Press Down to", fill="black", anchor="ms", font=font)
                d.text((120, 180), "Exit Scanning", fill="black", anchor="ms", font=font)
                d.text((120, 200), "And Start over again", fill="black", anchor="ms", font=font)
                d.text((120, 220), "__________________", fill="black", anchor="ms", font=font)
#        im = im.rotate()
                disp.image(im)
                time.sleep(0.25)
                break

#check size of image 
            imageload = sys.getsizeof(img.tobytes())
            print("img size in memory in bytes: ", imageload)
            if imageload >36000000:
                print("close but too big")
                time.sleep(1)
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
                im = Image.new("RGB", (240, 240), "red")
                d = ImageDraw.Draw(im)
#        d.line(((0, 120), (200, 120)), "gray")
#        d.line(((120, 0), (120, 200)), "gray")
                d.text((120, 80), "___(°)~(°)_________", fill="black", anchor="ms", font=font)
                d.text((120, 100), "DON'T do that", fill="black", anchor="rs", font=font)
                d.text((120, 120), "again", fill="black", anchor="ms", font=font)
                d.text((120, 140), "that NFT image file is", fill="black", anchor="ms", font=font)
                d.text((120, 160), "wayyy too big", fill="black", anchor="ms", font=font)
                d.text((120, 180), "Press down to start", fill="black", anchor="ms", font=font)
                d.text((120, 200), "over with a new file!", fill="black", anchor="ms", font=font)
                d.text((120, 220), "__________________", fill="black", anchor="ms", font=font)
#        im = im.rotate()
                disp.image(im)
                time.sleep(0.25)
                break
#                if imageload >36000000:
#                    raise stopIteration

#            except stopIteration:
#                print("close but too big")
#                break
            
            resized_img = img.resize((WIDTH, HEIGHT))
            try:
                disp.image(resized_img)
            except ValueError:
                print("GIF scan attempted")
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
                im = Image.new("RGB", (240, 240), "red")
                d = ImageDraw.Draw(im)
#        d.line(((0, 120), (200, 120)), "gray")
#        d.line(((120, 0), (120, 200)), "gray")
                d.text((120, 80), "___(°)~(°)_________", fill="black", anchor="ms", font=font)
                d.text((120, 100), "DON'T do that", fill="black", anchor="rs", font=font)
                d.text((120, 120), "NO GIFS", fill="black", anchor="ms", font=font)
                d.text((120, 140), "on this model", fill="black", anchor="ms", font=font)
                d.text((120, 160), "Press Down to", fill="black", anchor="ms", font=font)
                d.text((120, 180), "Exit Scanning", fill="black", anchor="ms", font=font)
                d.text((120, 200), "And Start over again", fill="black", anchor="ms", font=font)
                d.text((120, 220), "__________________", fill="black", anchor="ms", font=font)
#        im = im.rotate()
                disp.image(im)
                time.sleep(0.25)
                break
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
## clean or better interpret , and : characters in web links
## Add except if no qrcode was scanned

                #if qrcode text is currently not in our csv file, write timestampe and
                #qrcode to disk and update the set
            if qrcodeData not in found:
                csv2.write("{},{}\n".format(datetime.datetime.now(), qrcodeData))
                csv2.flush()
                found.add(qrcodeData)

        if buttonR.is_pressed:

#Splash: ALL Stored:  Resume Selecting Your NFT to display
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
            im = Image.new("RGB", (240, 240), "yellow")
            d = ImageDraw.Draw(im)
#                d.line(((0, 120), (200, 120)), "gray")
#                d.line(((120, 0), (120, 200)), "gray")

            d.text((120, 80), "___(°)~(°)_________", fill="black", anchor="ms", font=font)
            d.text((120, 100), "User:    ", fill="black", anchor="rs", font=font)
            d.text((120, 120), "Ended QRCodes scanning!", fill="black", anchor="ms", font=font)
            d.text((120, 140), "Press Left or", fill="black", anchor="ms", font=font)
            d.text((120, 160), "Right to select", fill="black", anchor="ms", font=font)
            d.text((120, 180), "your preferred NFT", fill="black", anchor="ms", font=font)
            d.text((120, 200), "to be displayed", fill="black", anchor="ms", font=font)
            d.text((120, 220), "__________________", fill="black", anchor="ms", font=font)
#    im = im.rotate(180)
            disp.image(im)
            time.sleep(0.25)
#set carousel at newest added nft: display new one here too?
            opened_file = open('qrcodes.csv')
            read_file = reader(opened_file)
            apps_data = list(read_file)
            x = (len(apps_data) - 1)
            print("Saved your punk")
            break
#set condition if no qrcode Data
#free camera object and exit
    cap.release()
    cv2.destroyAllWindows()
#    print(qrcodeData)



#    camera_on = not camera_on


def scroll_NFT():
    global apps_data
    global x
    x += 1
    if x > (len(apps_data) - 1):
        x = 0
    print("Your Saved Gan Punks")
    opened_file = open('qrcodes.csv')
    read_file = reader(opened_file)
    apps_data = list(read_file)
    onelink = apps_data[x][1]
    print(len(apps_data))

#display next NFT in order of CSV
    response = requests.get(onelink)
    image_bytes = io.BytesIO(response.content)
#check for bad link
    try:
        img = PIL.Image.open(image_bytes)
        resized_img = img.resize((WIDTH, HEIGHT))
        disp.image(resized_img)
        time.sleep(0.25)            
    except PIL.UnidentifiedImageError:
        print("Bad Link/File")

#    img = PIL.Image.open(image_bytes)
#    resized_img = img.resize((WIDTH, HEIGHT))
#    disp.image(resized_img)
#    time.sleep(0.25)

def reverse_scroll_NFT():
    global apps_data
    global x
#reverse direction scrolling
    print("Your Saved Gan Punks:reverse direction")
    x -= 1
    if x < 0:
        x = (len(apps_data) - 1) 
    opened_file = open('qrcodes.csv')
    from csv import reader
    read_file = reader(opened_file)
    apps_data = list(read_file)
    nftlinks = []
    onelink = apps_data[x][1]
    print(len(apps_data))

#display next NFT in reverse order of CSV
    response = requests.get(onelink)
    image_bytes = io.BytesIO(response.content)
#screen for bad link
    try:
        img = PIL.Image.open(image_bytes)
        resized_img = img.resize((WIDTH, HEIGHT))
        disp.image(resized_img)
        time.sleep(0.25)            
    except PIL.UnidentifiedImageError:
        print("Bad Link/File")

#    img = PIL.Image.open(image_bytes)
#    resized_img = img.resize((WIDTH, HEIGHT))
#    disp.image(resized_img)
#    time.sleep(0.25)


button1 = Button(21)
button2 = Button(20)
button3 = Button(16)

buttonL = Button(5)
buttonR = Button(26)
buttonU = Button(6) 
buttonD = Button(19)
buttonC = Button(13)

print("""
Pick your Gan Punk
""")

try: 
    button1.when_pressed = shut_down
    button2.when_pressed = delete_NFT
    button3.when_pressed = slideshow_mode
    buttonL.when_pressed = special_NFT
    buttonC.when_pressed = qr_capture
    buttonD.when_pressed = scroll_NFT
    buttonU.when_pressed = reverse_scroll_NFT
    pause()

finally:
    pass
