import pigpio
import time
from pca9685 import pca9685

PCA9685_ADDR = 0x40
pwm_freq = 50

pi = pigpio.pi()

servo_drv = pca9685( pi, PCA9685_ADDR )
servo_drv.set_freq( pwm_freq )

while True:
    servo_drv.set_pulse_t( 0, 1400 )
    time.sleep(5)
    servo_drv.set_pulse_t( 0, 1000 )
    time.sleep(5)
    servo_drv.set_pulse_t( 0, 1500 )
    time.sleep(5)
    servo_drv.set_pulse_t( 0, 1600 )
    time.sleep(5)
    servo_drv.set_pulse_t( 0, 2000 )
    time.sleep(5)
    servo_drv.set_pulse_t( 0, 1500 )
    time.sleep(5)

