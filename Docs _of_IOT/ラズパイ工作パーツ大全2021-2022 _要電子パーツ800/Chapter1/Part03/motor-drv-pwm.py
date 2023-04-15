import pigpio
import time

SPEED = 30

M1_PIN = 23
M2_PIN = 24

pi = pigpio.pi()

pi.set_mode( M1_PIN, pigpio.OUTPUT )
pi.set_PWM_frequency( M1_PIN, 50 )
pi.set_PWM_range( M1_PIN, 100 )

pi.set_mode( M2_PIN, pigpio.OUTPUT )
pi.set_PWM_frequency( M2_PIN, 50 )
pi.set_PWM_range( M2_PIN, 100 )



while True:
    pi.set_PWM_dutycycle( M1_PIN, SPEED )
    pi.set_PWM_dutycycle( M2_PIN, 0 )
    time.sleep( 5 )

    pi.set_PWM_dutycycle( M1_PIN, 0 )
    pi.set_PWM_dutycycle( M2_PIN, 0 )
    time.sleep( 5 )

    pi.set_PWM_dutycycle( M1_PIN, 0 )
    pi.set_PWM_dutycycle( M2_PIN, SPEED )
    time.sleep( 5 )

    pi.set_PWM_dutycycle( M1_PIN, 100 )
    pi.set_PWM_dutycycle( M2_PIN, 100 )
    time.sleep( 5 )
