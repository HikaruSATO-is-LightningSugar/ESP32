import pigpio
import time

ST_MOTOR_A0 = 18
ST_MOTOR_A1 = 23
ST_MOTOR_B0 = 24
ST_MOTOR_B1 = 25

STEPS = 200
SPEED = 0.01
DIRECT = 1

pi = pigpio.pi()

pi.set_mode( ST_MOTOR_A0, pigpio.OUTPUT )
pi.set_mode( ST_MOTOR_A1, pigpio.OUTPUT )
pi.set_mode( ST_MOTOR_B0, pigpio.OUTPUT )
pi.set_mode( ST_MOTOR_B1, pigpio.OUTPUT )

ST_MOTOR_OUT = [ 0b1100,
                 0b0110,
                 0b0011,
                 0b1001 ]

def to_bin( val ):
    if ( val == 0 ):
        return 0
    return 1

all_step = 0
finish = 0

while True:
    i = 0
    while ( i < len( ST_MOTOR_OUT ) ):
        if ( DIRECT  == 1 ):
            step_count = i
        else:
            step_count = len( ST_MOTOR_OUT ) - 1 - i

        a0 = to_bin( ST_MOTOR_OUT[ step_count ] & 0b1000 )
        a1 = to_bin( ST_MOTOR_OUT[ step_count ] & 0b0010 )
        b0 = to_bin( ST_MOTOR_OUT[ step_count ] & 0b0100 )
        b1 = to_bin( ST_MOTOR_OUT[ step_count ] & 0b0001 )

        print ( all_step, " : ", a0, a1, b0, b1 )

        pi.write( ST_MOTOR_A0, a0 )
        pi.write( ST_MOTOR_A1, a1 )
        pi.write( ST_MOTOR_B0, b0 )
        pi.write( ST_MOTOR_B1, b1 )

        time.sleep( SPEED )
        i = i + 1
        all_step = all_step + 1
        if ( STEPS <= all_step ):
            finish = 1
            break

    if ( finish == 1 ):
        break

