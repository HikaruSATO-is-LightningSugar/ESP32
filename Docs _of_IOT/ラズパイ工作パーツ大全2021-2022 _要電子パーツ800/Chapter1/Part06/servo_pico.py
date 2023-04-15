from machine import Pin, PWM
import time

SERVO_PIN = 16
PWM_FREQ = 50

def pulse_width( val, freq = PWM_FREQ, resol = 65535 ):
    pulse = freq * val * 1e-6 * resol
    return int( pulse )

servo = PWM( Pin( SERVO_PIN ) )
servo.freq( PWM_FREQ )

while True:
    duty = pulse_width( 1500 )
    servo.duty_u16( duty )
    time.sleep( 1 )
    
    duty = pulse_width( 500 )
    servo.duty_u16( duty )
    time.sleep( 1 )

    duty = pulse_width( 1500 )
    servo.duty_u16( duty )
    time.sleep( 1 )

    duty = pulse_width( 2500 )
    servo.duty_u16( duty )
    time.sleep( 1 )
