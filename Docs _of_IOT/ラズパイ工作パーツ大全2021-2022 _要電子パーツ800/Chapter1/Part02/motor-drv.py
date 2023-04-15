import pigpio
import time

M1_PIN = 23
M2_PIN = 24

pi = pigpio.pi()
pi.set_mode( M1_PIN, pigpio.OUTPUT )
pi.set_mode( M2_PIN, pigpio.OUTPUT )

while True:
    pi.write( M1_PIN, pigpio.HIGH )
    pi.write( M2_PIN, pigpio.LOW )
    time.sleep( 5 )

    pi.write( M1_PIN, pigpio.LOW )
    pi.write( M2_PIN, pigpio.LOW )
    time.sleep( 5 )

    pi.write( M1_PIN, pigpio.LOW )
    pi.write( M2_PIN, pigpio.HIGH )
    time.sleep( 5 )

    pi.write( M1_PIN, pigpio.HIGH )
    pi.write( M2_PIN, pigpio.HIGH )
    time.sleep( 5 )
