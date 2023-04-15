import pigpio
import time

PELTIER_PIN = 23

INTERVAL = 60

pi = pigpio.pi()
pi.set_mode( PELTIER_PIN, pigpio.OUTPUT )

while True:
    pi.write( PELTIER_PIN, pigpio.HIGH )
    time.sleep( INTERVAL )
    pi.write( PELTIER_PIN, pigpio.LOW )
    time.sleep( INTERVAL )



