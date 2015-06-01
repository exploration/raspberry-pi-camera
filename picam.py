#!/usr/bin/python

#######################################################################
# PiCam
#
# Written by Donald Merand + Andy Smith for Explo
# http://www.explo.org
# http://github.com/exploration
#######################################################################
import random
import RPi.GPIO as GPIO
import subprocess

cameraButtonPin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(cameraButtonPin, GPIO.IN)

# loop FOREVER
while True:
  buttonPressCheck = GPIO.input(cameraButtonPin)	
  if buttonPressCheck:
    grab_cam = subprocess.Popen("sudo raspistill -w 640 -h 480 -o /home/pi/raspberry-pi-camera/pictures/picture" + str(random.random()) + ".JPG", shell=True)
    grab_cam.wait()

  # wait a little bit, then try again
  time.sleep(0.5)
