import pigpio
import time

pi = pigpio.pi()

pi.set_mode( 23, pigpio.INPUT )
pi.set_pull_up_down( 23, pigpio.PUD_DOWN )

while True:
    if( pi.read( 23 ) == pigpio.HIGH ):
        print( "ON." )
    else:
        print( "OFF." )

    time.sleep( 1 )


