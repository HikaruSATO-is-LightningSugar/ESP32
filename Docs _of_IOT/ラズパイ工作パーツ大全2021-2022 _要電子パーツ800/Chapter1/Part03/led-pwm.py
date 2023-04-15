import pigpio

LED_PIN = 23
FREQ = 50

DUTY = 25

pi = pigpio.pi()

pi.set_mode( LED_PIN, pigpio.OUTPUT )
pi.set_PWM_frequency( LED_PIN, FREQ )
pi.set_PWM_range( LED_PIN, 100 )

pi.set_PWM_dutycycle( LED_PIN,  DUTY )




