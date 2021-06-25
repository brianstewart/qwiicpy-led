import qwiicpy_led as qpy


#  Option 1 (loading bar)
i=1
qpy.write_all_leds(0x00,0x00,0x0D)
qpy.wait(0.25)
while True:
    qpy.write_led(i,0x00,0x0D,0x00)
    qpy.wait(0.25)
    i+=1
    if i>=11:
        i=1
        qpy.write_all_leds(0x00,0x00,0x0D)
        qpy.wait(0.2)
