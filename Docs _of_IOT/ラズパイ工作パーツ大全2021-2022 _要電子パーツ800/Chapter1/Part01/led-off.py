import pigpio
import time

LED_PIN = 23

pi = pigpio.pi()

pi.set_mode( LED_PIN, pigpio.OUTPUT )

pi.write( LED_PIN, pigpio.LOW )


