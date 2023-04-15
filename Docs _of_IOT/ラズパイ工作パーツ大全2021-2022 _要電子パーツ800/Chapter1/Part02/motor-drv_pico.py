from machine import Pin
import time 

M1_PIN = 18
M2_PIN = 19

mot1 = Pin( M1_PIN, Pin.OUT )
mot2 = Pin( M2_PIN, Pin.OUT )

while True:
    mot1.value( 1 )
    mot2.value( 0 )
    time.sleep( 5 )

    mot1.value( 0 )
    mot2.value( 0 )
    time.sleep( 5 )

    mot1.value( 0 )
    mot2.value( 1 )
    time.sleep( 5 )

    mot1.value( 1 )
    mot2.value( 1 )
    time.sleep( 5 )
