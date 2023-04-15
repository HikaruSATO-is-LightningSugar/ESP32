# main.py -- put your code here!
import machine
import utime

led_pin = [13, 12, 14, 27, 26, 25, 33, 32]
pin_order = 0

while True:
    pin = 13
    #led = machine.Pin(led_pin[pin_order%len(led_pin)], machine.Pin.OUT)
    led = machine.Pin(pin, machine.Pin.OUT)
    led.value(1)
    utime.sleep(0.5)
    led.value(0)
    utime.sleep(0.5)
    pin_order += 1

