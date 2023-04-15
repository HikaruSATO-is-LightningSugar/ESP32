import pigpio
import time

STOP_ROT = 1
SPEED = 50
DIR = 1

divrot = 135

ROT_A_PIN = 23
ROT_B_PIN = 24
M1_PIN = 15
M2_PIN = 18

pi = pigpio.pi()

pi.set_mode( ROT_A_PIN, pigpio.INPUT )
pi.set_mode( ROT_B_PIN, pigpio.INPUT )
pi.set_mode( M1_PIN, pigpio.OUTPUT )
pi.set_mode( M2_PIN, pigpio.OUTPUT )
pi.set_PWM_frequency( M1_PIN, 50 )
pi.set_PWM_frequency( M2_PIN, 50 )
pi.set_PWM_range( M1_PIN, 100 )
pi.set_PWM_range( M2_PIN, 100 )

pi.set_PWM_dutycycle( M1_PIN, 0 )
pi.set_PWM_dutycycle( M2_PIN, 0 )

count = 0

stop_count = STOP_ROT * divrot

if ( DIR == 0 ):
    pi.set_PWM_dutycycle( M1_PIN, SPEED )
else:
    pi.set_PWM_dutycycle( M2_PIN, SPEED )

while True:
    if( pi.read( ROT_A_PIN ) == pigpio.HIGH ):
        while True:
            if( pi.read( ROT_A_PIN ) == pigpio.LOW ):
                break
        count = count + 1
        if ( count > stop_count ):
            pi.set_PWM_dutycycle( M1_PIN, 0 )
            pi.set_PWM_dutycycle( M2_PIN, 0 )
            break




