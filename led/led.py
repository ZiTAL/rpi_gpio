#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# root moduan exekutatu

import RPi.GPIO as GPIO  
import time  

# blinking function  
def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(1)  
        return True

# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)  

# set up GPIO output channel  
GPIO.setup(11, GPIO.OUT)  

# blink GPIO17 10 times  
for i in range(0, 10):  
        blink(11)

GPIO.cleanup() 
