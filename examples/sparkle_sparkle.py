#!/usr/bin/python3

from random import random,randint
import qwiicpy_led as qpy

qpy.write_all_leds_off()
qpy.write_all_leds_brightness(1)

ttl = [0]*10
while True:
    for i in range(0,10):
        if ttl[i] == 0:
            if random() > 0.9:
                ttl[i] = randint(1,3)
                qpy.write_led(i+1,200,200,200)
        else:
            ttl[i] -= 1
            if ttl[i] == 0: qpy.write_led(i+1,0,0,0)
    qpy.wait(.125)
