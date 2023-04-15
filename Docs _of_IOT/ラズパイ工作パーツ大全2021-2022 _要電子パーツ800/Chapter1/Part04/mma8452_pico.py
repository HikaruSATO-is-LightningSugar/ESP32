from machine import Pin, I2C
import time, math

class mma8452:
    def __init__( self, i2c, addr ):
        self.addr = addr
        self.i2c = i2c
        self.range = 2

    def begin( self, range ):
        self.range = range
        tmp = self.i2c.readfrom_mem( self.addr, 0x2a, 1 )[0]
        self.i2c.writeto_mem( self.addr, 0x2a, bytes([int( tmp & 0xfe )]) )

        self.i2c.writeto_mem( self.addr, 0x0e, bytes([int( range >> 2 )]) )

        tmp = self.i2c.readfrom_mem( self.addr, 0x2a, 1 )[0]
        self.i2c.writeto_mem( self.addr, 0x2a, bytes([int( tmp | 0x01 )]) )

        tmp = self.i2c.readfrom_mem( self.addr, 0x2a, 1 )[0]

    def get_accel( self ):
        data = self.i2c.readfrom_mem( self.addr, 0x01, 6 )
    
        x_accel = ( data[0] << 4 ) | ( data[1] >> 4 )
        if( x_accel > 2047 ):
            x_accel = x_accel - 4096

        y_accel = ( data[2] << 4 ) | ( data[3] >> 4 )
        if( y_accel > 2047 ):
            y_accel = y_accel - 4096

        z_accel = ( data[4] << 4 ) | ( data[5] >> 4 )
        if( z_accel > 2047 ):
            z_accel = z_accel - 4096
    
        return( - x_accel, - y_accel, - z_accel )

    def conv_angle( self, x, y, z ):
        x_angle = math.degrees( math.atan2( x, math.sqrt( y ** 2 + z ** 2 ) ) )
        y_angle = math.degrees( math.atan2( y, math.sqrt( x ** 2 + z ** 2 ) ) )
        return ( x_angle, y_angle )
