import pigpio
import time

PINT_PIN = 23

pi = pigpio.pi()

pi.set_mode( PINT_PIN, pigpio.INPUT )
pi.set_pull_up_down( PINT_PIN, pigpio.PUD_OFF )

count = 0

while ( True ):
    if ( pi.read( PINT_PIN ) == pigpio.HIGH ):
        time.sleep( 0.01 )
        count = count + 1
        print( "Count : {}".format( count ) )
        while( pi.read( PINT_PIN ) == pigpio.HIGH ):
            time.sleep( 0.01 )

