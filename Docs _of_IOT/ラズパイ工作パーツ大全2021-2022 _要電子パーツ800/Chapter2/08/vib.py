import pigpio
import time

M_PIN = 23

PATTERN = [ 1, 1, 2, 1, 3 ]

pi = pigpio.pi()
pi.set_mode( M_PIN, pigpio.OUTPUT )
pi.write( M_PIN, pigpio.LOW )

output = pigpio.HIGH

for data in PATTERN:
    pi.write( M_PIN, output )
    time.sleep( data )
    if ( output == pigpio.HIGH ):
        output = pigpio.LOW
    else:
        output = pigpio.HIGH

pi.write( M_PIN, pigpio.LOW )

