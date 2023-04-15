from machine import Pin, PWM

M_PIN = 18
SPEED = 30

FREQ = 50

motor = PWM( Pin( M_PIN ) )

motor.freq( FREQ )

pwm_out = int( SPEED / 100 * 65535 )

motor.duty_u16( pwm_out )

