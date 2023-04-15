import pigpio
import time

M_PIN = 23

pi = pigpio.pi()
pi.set_mode( M_PIN, pigpio.OUTPUT )

while True:
    pi.write( M_PIN, pigpio.HIGH )
    time.sleep ( 5 )
    pi.write( M_PIN, pigpio.LOW )
    time.sleep ( 5 )

