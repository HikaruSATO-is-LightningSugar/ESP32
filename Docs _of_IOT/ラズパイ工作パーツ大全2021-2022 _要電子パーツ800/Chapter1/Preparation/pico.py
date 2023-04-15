from machine import Pin
import time

ledpin = 25

led = Pin( ledpin, Pin.OUT )

status = 0
while True:
    status = abs( status - 1 )
    led.value ( status )

    if( status == 0 ):
        print( "LED OFF." ) 
    else:
        print( "LED ON." )
    time.sleep( 1 )
