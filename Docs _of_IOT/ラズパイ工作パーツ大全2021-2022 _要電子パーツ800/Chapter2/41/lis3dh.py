import pigpio
import time, math

class lis3dh:
    def __init__( self, handle, ch, addr, range=2 ):
        self.addr = addr
        self.ch = ch
        self.pi = handle

        self.gravity = 9.80665

        self.i2c = self.pi.i2c_open( self.ch, self.addr )
        
        self.pi.i2c_write_byte_data( self.i2c, 0x24, 0x80 )
        time.sleep(0.01)
        self.pi.i2c_write_byte_data( self.i2c, 0x20, 0x77 )
        self.pi.i2c_write_byte_data( self.i2c, 0x23, 0x88 )
        self.pi.i2c_write_byte_data( self.i2c, 0x24, 0x08 )

        if( range == 4 ):
            self.range = 4
            self.dev = 8190
            self.range_ctrl = 0b01
        elif( range == 8 ):
            self.range = 8
            self.dev = 4096
            self.range_ctrl = 0b10
        elif( range == 16 ):
            self.range = 16
            self.dev = 1365
            self.range_ctrl = 0b11
        else:
            self.range = 2
            self.dev = 16380
            self.range_ctrl = 0b00


        reg_val = self.pi.i2c_read_byte_data( self.i2c, 0x23 )
        reg_val = ( reg_val & 0b11001111 ) | ( self.range_ctrl << 4 ) 
        self.pi.i2c_write_byte_data( self.i2c, 0x23, reg_val )


    def conv_two_byte( self, high, low ):
        dat = high << 8 | low
        if ( high >= 0x80 ):
            dat = dat - 0xffff
        return ( dat )

    def conv_angle( self, x, y, z ):
        x_angle = math.degrees( math.atan2( x, math.sqrt( y ** 2 + z ** 2 ) ) )
        y_angle = math.degrees( math.atan2( y, math.sqrt( x ** 2 + z ** 2 ) ) )
        return ( x_angle, y_angle )

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
    
    def read_g( self ):
        ( x, y, z ) = self.read_data()
        gx = x / self.dev
        gy = y / self.dev
        gz = z / self.dev
        return ( gx, gy, gz )

    def read_accel( self ):
        ( x, y, z ) = self.read_data()
        ax = x / self.dev * self.gravity
        ay = y / self.dev * self.gravity
        az = z / self.dev * self.gravity
        return ( ax, ay, az )



