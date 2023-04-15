import pigpio
import time

PIR_PIN = 23

pi = pigpio.pi()

pi.set_mode( PIR_PIN, pigpio.INPUT )
pi.set_pull_up_down( PIR_PIN, pigpio.PUD_OFF )

while ( True ):
    if ( pi.read( PIR_PIN ) == pigpio.HIGH ):
        print ( "Visitor." )
    else:
        print ( "Nobody." )

    time.sleep( 1 )


