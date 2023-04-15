import pigpio
import time

HT16K33_ADDR = 0x70

matrix_row = 7
i2c_channel = 1


pattern = [ 0b00010,
            0b01010,
            0b01010,
            0b01010,
            0b11111,
            0b11111,
            0b01110 ]

def matrix_write( pi, pattern ):
    row = 0
    while ( row < matrix_row ):
        pi.i2c_write_byte_data( i2c, row * 2, pattern[row] )
        row = row + 1


pi = pigpio.pi()
i2c = pi.i2c_open( i2c_channel, HT16K33_ADDR )

pi.i2c_write_byte_data( i2c, 0x21, 0x01 )
pi.i2c_write_byte_data( i2c, 0x81, 0x01 )
time.sleep(0.1)

matrix_write( pi, pattern )

