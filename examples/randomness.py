#!/usr/bin/python3

from random import randint
import qwiicpy_led as qpy

qpy.write_all_leds_brightness(1)

while True:
    qpy.write_all_leds(randint(0,255),randint(0,255),randint(0,255))
    qpy.wait(0.50)
