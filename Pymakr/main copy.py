import machine
import utime
 
list_of_pin = [13, 12, 14, 27, 25, 26, 33, 32]
pin_order = 0
while True:
     #led_pin = list_of_pin[pin_order % (len(list_of_pin) + 1)]
    led_pin = 32
    led = machine.Pin(led_pin, machine.Pin.OUT)
    led.value(1)
    utime.sleep(0.5)
    led.value(0)
    pin_order += 1
