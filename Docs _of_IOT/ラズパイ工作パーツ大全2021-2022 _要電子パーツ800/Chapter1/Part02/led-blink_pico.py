from machine import Pin
import time 

LED_PIN = 18

led = Pin( LED_PIN, Pin.OUT )

while True:
    led.value( 0 )
    time.sleep( 1 )

    led.value( 1 )
    time.sleep( 1 )
    