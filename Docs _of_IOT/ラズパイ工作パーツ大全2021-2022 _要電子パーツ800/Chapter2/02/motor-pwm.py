import pigpio

SPEED = 50

M_PIN = 23
pi = pigpio.pi()
pi.set_mode( M_PIN, pigpio.OUTPUT )
pi.set_PWM_frequency( M_PIN, 50 )
pi.set_PWM_range( M_PIN, 100 )

pi.set_PWM_dutycycle( M_PIN, SPEED )

