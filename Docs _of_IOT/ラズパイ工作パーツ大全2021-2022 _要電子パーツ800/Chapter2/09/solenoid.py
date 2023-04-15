import pigpio
import time

S_PIN = 23

pi = pigpio.pi()
pi.set_mode( S_PIN, pigpio.OUTPUT )

pi.write( S_PIN, pigpio.HIGH )

time.sleep( 10 )

pi.write( S_PIN, pigpio.LOW )

