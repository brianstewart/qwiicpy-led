from random import random,randint
import qwiicpy_led as qpy


qpy.write_all_leds_brightness(1)
qpy.write_color_array(
                      [0,0,150,150,0,0,150,150,0,0],
                      [150,0,0,0,150,0,0,0,150,0],
                      [0,150,150,0,0,150,150,0,0,150]
)

ttl=[0]*10
while True:
    for i in range(0,10):
        if ttl[i] == 0:
            if random() > 0.5:
                ttl[i] = randint(1,3)
                qpy.write_led_brightness(i+1,2)
        else:
            ttl[i] -= 1
            if ttl[i] == 0: qpy.write_led_brightness(i+1,1)
    qpy.wait(0.125)
