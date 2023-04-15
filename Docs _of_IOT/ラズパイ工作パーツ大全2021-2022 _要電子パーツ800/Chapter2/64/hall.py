import pigpio
import time

HALL_PIN = 23

pi = pigpio.pi()

pi.set_mode( HALL_PIN, pigpio.INPUT )
pi.set_pull_up_down( HALL_PIN, pigpio.PUD_OFF )

while ( True ):
    if ( pi.read( HALL_PIN ) == pigpio.HIGH ):
        print ( "S Pole." )
    else:
        print ( "N Pole." )

    time.sleep( 0.5 )


