import time
import pigpio

SENSOR_PIN = 23

pi = pigpio.pi()

pi.set_mode( SENSOR_PIN, pigpio.INPUT )
pi.set_pull_up_down( SENSOR_PIN, pigpio.PUD_OFF )

mode = 0

while True:
    if( pi.read( SENSOR_PIN ) == pigpio.HIGH ):
        mode = abs( mode - 1 )
        if ( mode == 0 ):
            print( "Off." )
        else:
            print( "On." )

        while ( pi.read( SENSOR_PIN ) == pigpio.HIGH ):
            time.sleep( 0.1 )


