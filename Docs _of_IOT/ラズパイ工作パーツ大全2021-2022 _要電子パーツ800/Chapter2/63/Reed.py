import time
import pigpio

SENSOR_PIN = 23

pi = pigpio.pi()

pi.set_mode( SENSOR_PIN, pigpio.INPUT )
pi.set_pull_up_down( SENSOR_PIN, pigpio.PUD_UP )

while True:
    if( pi.read( SENSOR_PIN ) == pigpio.LOW ):
        print( "Close.")
    else:
        print( "Open.")
    
    time.sleep( 1 )


