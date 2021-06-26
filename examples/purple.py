#!/usr/bin/python3

import qwiicpy_led as qpy

BRIGHT = 1

qpy.write_all_leds(30,0,60)
qpy.write_all_leds_brightness(BRIGHT)

qpy.write_led_brightness(4,BRIGHT*2)
qpy.write_led_brightness(5,BRIGHT*2)
qpy.write_led_brightness(6,BRIGHT*2)
i=7
trail_i=4
while True:
    qpy.write_led_brightness(i,BRIGHT*3)
    qpy.write_led_brightness(trail_i,BRIGHT)
    qpy.wait(.125)
    i+=1
    if i>10: i=1
    trail_i+=1
    if trail_i>10: trail_i=1
