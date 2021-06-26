#!/usr/bin/python3

import qwiicpy_led as qpy

qpy.write_all_leds(0x00,0x00,0x0D)
i=0
r=0x00
g=0x0D
b=0x00
while True:
    qpy.write_led(10-i,r,g,b)
    qpy.wait(0.125)
    qpy.write_led(10-i,0x00,0x00,0x0D)
    i+=1
    if i>=10:i=0
