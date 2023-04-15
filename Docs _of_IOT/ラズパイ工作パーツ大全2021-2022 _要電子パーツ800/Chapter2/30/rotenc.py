import pigpio
import time

ROT_A_PIN = 23
ROT_B_PIN = 24

pi = pigpio.pi()

pi.set_mode( ROT_A_PIN, pigpio.INPUT )
pi.set_pull_up_down( ROT_A_PIN, pigpio.PUD_UP )
pi.set_mode( ROT_B_PIN, pigpio.INPUT )
pi.set_pull_up_down( ROT_B_PIN, pigpio.PUD_UP )

count = 0

b_a = pigpio.HIGH
b_b = pigpio.HIGH
buf = [ 0, 0, 0, 0 ]

while True:
    flag = 0
    a = pi.read( ROT_A_PIN )
    b = pi.read( ROT_B_PIN )
    time.sleep( 0.001 )
    
    if ( b_a != a or b_b != b ):
        del buf[0]
        buf.append( b_a * 8 + b_b * 4 + a * 2 + b )
        b_a = a
        b_b = b
        if ( buf == [ 0b1101, 0b0100, 0b0010, 0b1011 ] ):
            count = count + 1
            flag = 1
        if ( buf == [ 0b1110, 0b1000, 0b0001, 0b0111 ] ):
            count = count - 1
            flag = 1
    if ( flag == 1 ):
        print( "Positions: {:}  Angle: {:} ".format( count, count * 15 ) )

