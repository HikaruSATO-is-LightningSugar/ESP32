import pigpio
import time

FALL_PIN = 23

pi = pigpio.pi()

pi.set_mode( FALL_PIN, pigpio.INPUT )
pi.set_pull_up_down( FALL_PIN, pigpio.PUD_UP )

while ( True ):
    if ( pi.read( FALL_PIN ) == pigpio.HIGH ):
        print ( "Fall down." )
    else:
        print ( "Stability." )

    time.sleep( 1 )


