from machine import Pin, PWM
import time

M1_PIN = 18
M2_PIN = 19
SPEED = 30

FREQ = 50

mot1 = PWM( Pin( M1_PIN ) )
mot2 = PWM( Pin( M2_PIN ) )

mot1.freq( FREQ )
mot2.freq( FREQ )

out_speed = int( SPEED / 100 * 65535 )

while True:
    mot1.duty_u16( out_speed )
    mot2.duty_u16( 0 )
    time.sleep( 5 )

    mot1.duty_u16( 0 )
    mot2.duty_u16( 0 )
    time.sleep( 5 )

    mot1.duty_u16( 0 )
    mot2.duty_u16( out_speed )
    time.sleep( 5 )

    mot1.duty_u16( 65535 )
    mot2.duty_u16( 65535 )
    time.sleep( 5 )



