from machine import Pin
import time 

M_PIN = 18

mot = Pin( M_PIN, Pin.OUT )

while True:
    mot.value( 1 )
    time.sleep( 5 )

    mot.value( 0 )
    time.sleep( 5 )
    