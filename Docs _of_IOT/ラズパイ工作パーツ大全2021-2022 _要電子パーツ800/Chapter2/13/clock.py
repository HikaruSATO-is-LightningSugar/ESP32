import pigpio
import time, datetime

HT16K33_ADDR = 0x70
I2C_CH = 1

DIGIT = 4

dot = [ 0, 0, 0, 0 ]
colon_up = 0
colon_down = 0
dot_up = 0

seg_char = [ 0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7c, 0x07, 0x7f, 0x67 ]

pi = pigpio.pi()
i2c = pi.i2c_open( I2C_CH, HT16K33_ADDR )

pi.i2c_write_byte_data( i2c, 0x21, 0x01)
pi.i2c_write_byte_data( i2c, 0x81, 0x01)

def makedigit( hour, min ):
    dig = [ 0, 0, 0, 0 ]
    if ( hour < 9 ):
        dig[0] = 0
        dig[1] = hour
    else:
        dig[0] = int( hour / 10 )
        dig[1] = hour - dig[0] * 10

    if ( min < 9 ):
        dig[2] = 0
        dig[3] = min
    else:
        dig[2] = int( min / 10 )
        dig[3] = min - dig[2] * 10

    return( dig )


b_hour = 0
b_min = 0
b_sec = 0

while True:
    dt = datetime.datetime.now()
    if( b_min != dt.minute or b_hour != dt.hour ):
        b_min = dt.minute
        b_hour = dt.hour
        out_dig = makedigit( dt.hour, dt.minute )

        i = 0
        while( i < DIGIT ):
            pi.i2c_write_byte_data( i2c, i * 2, seg_char[ out_dig[i] ] )
            i = i + 1

    if( b_sec != dt.second ):
        b_sec = dt.second
        out_col = dt.second % 2
        pi.i2c_write_byte_data( i2c, 8, out_col + out_col * 2 + dot_up * 4 )

    time.sleep(0.1)




