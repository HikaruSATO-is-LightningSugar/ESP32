from machine import Pin
import time

class ledblink():
    def __init__( self, pin = 25, interval = 1 ):
        self.ledpin = pin
        self.inter = interval
        
        self.led = Pin( self.ledpin, Pin.OUT )

    def blink( self, count = 10 ):
        i = 0
        while ( i < count ):
            self.led.value( 1 )
            time.sleep( self.inter )
            self.led.value( 0 )
            time.sleep( self.inter )
            i = i + 1
            
