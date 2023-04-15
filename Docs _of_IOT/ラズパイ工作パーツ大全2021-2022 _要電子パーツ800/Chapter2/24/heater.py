import pigpio
import time

HEATER_PIN = 23

TIMER = 300

pi = pigpio.pi()

pi.set_mode( HEATER_PIN, pigpio.OUTPUT )

pi.write( HEATER_PIN, pigpio.HIGH )

time.sleep( TIMER )

pi.write( HEATER_PIN, pigpio.LOW )



