from machine import Pin, PWM

LED_PIN = 18
FREQ = 50

DUTY = 25

led = PWM( Pin( LED_PIN ) )

led.freq( FREQ )

pwm_out = int( DUTY / 100 * 65535 )

led.duty_u16( pwm_out )
