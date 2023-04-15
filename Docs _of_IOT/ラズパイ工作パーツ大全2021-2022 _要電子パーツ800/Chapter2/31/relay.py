import pigpio
import time

RELAY_PIN = 23

TIMER = 180

pi = pigpio.pi()

pi.set_mode( RELAY_PIN, pigpio.OUTPUT )

pi.write( RELAY_PIN, pigpio.HIGH )
time.sleep( TIMER )
pi.write( RELAY_PIN, pigpio.LOW )


