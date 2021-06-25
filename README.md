################
    README
################

Module Author: Brian Stewart

This module (qwiicpy) was created to control the Qwiic LED Stick using Raspberry Pi GPIO pins

---------------------------------------------------------------------------------------------------

The product page can be found at the following link: https://www.sparkfun.com/products/14783
The code library written for Arduino implementation here: https://github.com/sparkfun/SparkFun_Qwiic_LED_Stick_Arduino_Library
And finally the firmware code for the LED stick here: https://github.com/sparkfunX/Qwiic_LED_Stick/blob/master/Firmware/Qwiic_LED_Stick/Qwiic_LED_Stick.ino

---------------------------------------------------------------------------------------------------

The firmware code serves as the source for all command addresses as well as the write data required for each command

---------------------------------------------------------------------------------------------------

# Pinout Instructions
Using the Qwiic Cable - Breadboard Jumper: https://www.sparkfun.com/products/14425
Red Wire    -> 3.3V   to Rpi Pin1
Black Wire  -> Ground to Rpi Pin6
Blue Wire   -> SDA    to Rpi Pin3 (GPIO/BCM 2)
Yellow Wire -> SCL    to Rpi Pin5 (GPIO/BCM 3)
