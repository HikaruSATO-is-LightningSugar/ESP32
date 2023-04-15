import pigpio
import time, math

class l3gd20h:
    def __init__( self, handle, ch, addr, range=0 ):
        self.addr = addr
        self.ch = ch
        self.pi = handle

        self.i2c = self.pi.i2c_open( self.ch, self.addr )
        
        self.pi.i2c_write_byte_data( self.i2c, 0x20, 0x0f )
        time.sleep(0.01)
        self.pi.i2c_write_byte_data( self.i2c, 0x21, 0x00 )
        self.pi.i2c_write_byte_data( self.i2c, 0x22, 0x00 )
        self.pi.i2c_write_byte_data( self.i2c, 0x23, 0x00 )
        self.pi.i2c_write_byte_data( self.i2c, 0x24, 0x00 )

        if( range == 1 ):
            self.range = 1
            self.dev = 0.0175
            self.range_ctrl = 0b01
        elif( range == 2 ):
            self.range = 2
            self.dev = 0.07
            self.range_ctrl = 0b10
        else:
            self.range = 0
            self.dev = 0.00875
            self.range_ctrl = 0b00

        reg_val = self.pi.i2c_read_byte_data( self.i2c, 0x23 )
        reg_val = ( reg_val & 0b11001111 ) | ( self.range_ctrl << 4 ) 
        self.pi.i2c_write_byte_data( self.i2c, 0x23, reg_val )


    def conv_two_byte( self, high, low ):
        dat = high << 8 | low
        if ( high >= 0x80 ):
            dat = dat - 0xffff
        return ( dat )

    def read_data( self ):
        lb = self.pi.i2c_read_byte_data( self.i2c, 0x28 )
        hb = self.pi.i2c_read_byte_data( self.i2c, 0x29 )
        x = self.conv_two_byte( hb, lb )

        lb = self.pi.i2c_read_byte_data( self.i2c, 0x2a )
        hb = self.pi.i2c_read_byte_data( self.i2c, 0x2b )
        y = self.conv_two_byte( hb, lb )

        lb = self.pi.i2c_read_byte_data( self.i2c, 0x2c )
        hb = self.pi.i2c_read_byte_data( self.i2c, 0x2d )
        z = self.conv_two_byte( hb, lb )
    
        return ( x, y, z )
    
    def get_dps( self ):
        ( x, y, z ) = self.read_data()
        dx = x * self.dev
        dy = y * self.dev
        dz = z * self.dev
        return ( dx, dy, dz )
