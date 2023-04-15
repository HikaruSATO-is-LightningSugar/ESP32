import pigpio
import time

pi = pigpio.pi()

pi.set_mode( 18, pigpio.OUTPUT )

while True:
    pi.write( 18, pigpio.HIGH )
    time.sleep( 1 )

    pi.write( 18, pigpio.LOW )
    time.sleep( 1 )

