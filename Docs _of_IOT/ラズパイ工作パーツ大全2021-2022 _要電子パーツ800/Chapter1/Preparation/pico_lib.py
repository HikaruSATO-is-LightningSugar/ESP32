from machine import Pin
from ledblink import ledblink

ledpin = 25
interval = 0.5
count = 10

led = ledblink( ledpin, interval )

led.blink( count )
