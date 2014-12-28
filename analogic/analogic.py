#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# su
# aptitude install python2.7-dev
# aptitude install python-pip
# pip install spidev
#
# comment "blacklist spi-bcm2708" in /etc/modprobe.d/raspi-blacklist.conf and reboot

import spidev
import time
import os

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
        adc = spi.xfer2([1,(8+channel)<<4,0])
        data = ((adc[1]&3) << 8) + adc[2]
        return data

# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data, places, v):
        volts = (data * v) / float(1023)
        volts = round(volts,places)
        return volts

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Define sensor channels
light_channel = 0
pot_channel = 1

# Define delay between readings
delay = 1

# Defile Volts 5 or 3.3
volts = 5

while True:
        # Read the light sensor data
        light_level = ReadChannel(light_channel)
        light_volts = ConvertVolts(light_level, 2, volts)

        # Read potencimeter
        pot_level = ReadChannel(pot_channel)
        pot_volts = ConvertVolts(pot_level, 2, volts)

        # Print out results
        print("Light: {} ({}V)".format(light_level, light_volts))
        print("Potenciometer: {} ({}V)".format(pot_level, pot_volts))
        print "--------------------------------------------"

        # Wait before repeating loop
        time.sleep(delay)
