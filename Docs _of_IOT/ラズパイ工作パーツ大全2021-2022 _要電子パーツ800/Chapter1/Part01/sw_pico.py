from machine import Pin
import time

SW_PIN = 15

sw = Pin( SW_PIN, Pin.IN )

while True:
    if( sw.value() == 1 ):
        print( "ON." )
    else:
        print( "OFF." )
        
    time.sleep( 0.5 )
