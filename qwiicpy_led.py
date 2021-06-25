#!/usr/bin/python3

##############################
##
## Sparkfun QWIIC LED Stick
## Product Page -> https://www.sparkfun.com/products/14783
## Arduino code & examples found here -> https://github.com/sparkfun/SparkFun_Qwiic_LED_Stick_Arduino_Library
## Firmware code for stick found here -> https://github.com/sparkfunX/Qwiic_LED_Stick/blob/master/Firmware/Qwiic_LED_Stick/Qwiic_LED_Stick.ino
##
##############################

## NOTES FROM FIRMWARE CODE  ##
## I2C Default Stick Address
_I2C_ADDR = 0x23

## I2C Command Codes
_CMD_WRITE_SINGLE_LED_COLOR      = 0x71
_CMD_WRITE_ALL_LEDS_COLOR        = 0x72
_CMD_WRITE_RED_ARRAY             = 0x73
_CMD_WRITE_GREEN_ARRAY           = 0x74
_CMD_WRITE_BLUE_ARRAY            = 0x75
_CMD_WRITE_SINGLE_LED_BRIGHTNESS = 0x76
_CMD_WRITE_ALL_LEDS_BRIGHTNESS   = 0x77
_CMD_WRITE_ALL_LEDS_OFF          = 0x78

from time import sleep as _sleep
from smbus import SMBus as _SMBus

_DEFAULT_AMP = 4    #  Default brightness level
_amps = [_DEFAULT_AMP]*10    #  Stores brightness level of each led

def wait(secs):
    """
    Pass-through function calls the sleep method from the time module
    Convenience function so the time module does not need to be imported twice
    secs -> number of seconds to pause; can be a decimal number for partial seconds
    """
    _sleep(secs)

def write_led(addr, r, g, b):
    """
    Write a color to a single LED
    addr -> 1 byte (values 1-10 for a single stick)
    r,g,b -> 1 byte each
    """
    _bus.write_i2c_block_data(_I2C_ADDR, _CMD_WRITE_SINGLE_LED_COLOR, [addr, r, g, b])

def write_all_leds(r, g, b):
    """
    Write a color to all LEDs
    r,g,b -> 1 byte each
    """
    _bus.write_i2c_block_data(_I2C_ADDR, _CMD_WRITE_ALL_LEDS_COLOR, [r, g, b])

def write_color_array(r, g, b, length=0x0A, offset=0x00):
    """
    Write RGB values to all LEDs using an array for each color value of length equal to the LED count (10)
    r,g,b -> array of 1 bytes each - each color array requires a length byte (10), offset byte (default 0), and then a color byte for each LED
    """
    _bus.write_i2c_block_data(_I2C_ADDR, _CMD_WRITE_RED_ARRAY, [length, offset,]+r)
    _sleep(0.006)    #  I've found issues with colors not lighting up appropriately if these arrays are written too close to each other
    _bus.write_i2c_block_data(_I2C_ADDR, _CMD_WRITE_GREEN_ARRAY, [length, offset,]+g)
    _sleep(0.006)
    _bus.write_i2c_block_data(_I2C_ADDR, _CMD_WRITE_BLUE_ARRAY, [length, offset,]+b)

def write_led_brightness(addr, amp):
    """
    Write brightness value to a single LED
    addr -> 1 byte (values 1-10 for a single stick)
    amp -> 1 byte (3 most significant bits must be 0 allowing a value range of 0-31 or max 0b00011111)
    """
    global _amps
    _bus.write_i2c_block_data(_I2C_ADDR, _CMD_WRITE_SINGLE_LED_BRIGHTNESS, [addr, amp])
    _amps[addr-1] = amp

def write_all_leds_brightness(amp):
    """
    Write brightness value to all LEDs
    amp -> 1 byte (3 most significant bits must be 0 allowing a value range of 0-31 or max 0b00011111)
    """
    global _amps
    _bus.write_i2c_block_data(_I2C_ADDR, _CMD_WRITE_ALL_LEDS_BRIGHTNESS, [amp])
    _amps = [amp for x in _amps]

def write_brightness_array(amps):
    """
    Write individual brightness values to each LED
    amps -> array of 1 byte brightness values (0-31) for each LED
    """
    global _amps
    for i in range(0,10):
        write_led_brightness(i+1,amps[i])
    _amps = amps

def write_all_leds_off():
    """
    Write all LEDs to color 0 to turn them off
    """
    _bus.write_i2c_block_data(_I2C_ADDR, _CMD_WRITE_ALL_LEDS_OFF, [])

def blink_leds(secs):
    """
    Turn off all LED brightness for a specified amount of time and then return color at specified brightness level
    amp -> brightness level post blink
    secs -> seconds to blink for
    """
    amps = _amps
    write_all_leds_brightness(0)
    _sleep(secs)
    write_brightness_array(amps)

def hide():
    """
    Hide LED lights indefinitely by setting brightness to 0; this is different than write_all_leds_off() as you can unhide them to restore the previous display
    """
    global _amps
    amps = _amps
    write_all_leds_brightness(0)
    _amps = amps

def unhide():
    """
    Restores hidden display
    """
    write_brightness_array(_amps)

def reset_stick():
    """
    Reset LED to our default on state
    """
    write_all_leds_brightness(_DEFAULT_AMP)    #  Tone the brightness down before setting any colors (This thing can get bright!)
    write_all_leds(0x00,0x0F,0x00)
    _sleep(0.4)
    blink_leds(0.4)
    _sleep(0.4)
    blink_leds(0.4)
    _sleep(0.75)


#  Initialize
_bus = _SMBus(1)
_sleep(0.5)    #  Let I2C settle to avoid 121 IO Error
#reset_stick()
