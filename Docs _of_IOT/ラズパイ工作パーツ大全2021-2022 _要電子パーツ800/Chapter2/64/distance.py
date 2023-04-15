import pigpio
import time

diameter = 0.71

HALL_PIN = 23

pi = pigpio.pi()

pi.set_mode( HALL_PIN, pigpio.INPUT )
pi.set_pull_up_down( HALL_PIN, pigpio.PUD_OFF )

pole = pigpio.HIGH
count = 0

while ( True ):
    sensor = pi.read( HALL_PIN )
    if ( pole != sensor ):
        count = count + 0.5
        dist = diameter * 3.14 * count
        print ( "Distance: {:.1f}m ".format( dist ) )
        pole = sensor
        time.sleep( 0.1 )
