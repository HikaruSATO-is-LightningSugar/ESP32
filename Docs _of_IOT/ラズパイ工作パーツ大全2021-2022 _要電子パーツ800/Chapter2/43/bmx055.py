import pigpio
import time, math

class bmx055:
    def __init__( self, pi, i2c_ch, accel_addr, comp_addr, gyro_addr ):
        self.pi = pi
        self.accel_addr = accel_addr
        self.comp_addr = comp_addr
        self.gyro_addr = gyro_addr
        self.i2c_ch = i2c_ch
        self.i2c_accel = self.pi.i2c_open( self.i2c_ch, self.accel_addr )
        self.i2c_comp = self.pi.i2c_open( self.i2c_ch, self.comp_addr )
        self.i2c_gyro = self.pi.i2c_open( self.i2c_ch, self.gyro_addr )

        self.calib_x = 0
        self.calib_y = 0
        
        self.pi.i2c_write_byte_data( self.i2c_accel, 0x0f, 0x03 )
        time.sleep(0.1)

        self.pi.i2c_write_byte_data( self.i2c_accel, 0x10, 0x08 )
        time.sleep(0.1)

        self.pi.i2c_write_byte_data( self.i2c_accel, 0x11, 0x00 )
        time.sleep(0.1)
        
        self.pi.i2c_write_byte_data( self.i2c_gyro, 0x0f, 0x04 )
        time.sleep(0.1)
        
        self.pi.i2c_write_byte_data( self.i2c_gyro, 0x10, 0x07 )
        time.sleep(0.1)

        self.pi.i2c_write_byte_data( self.i2c_gyro, 0x11, 0x00 )
        time.sleep(0.1)

        self.pi.i2c_write_byte_data( self.i2c_comp, 0x4b, 0x83 )
        time.sleep(0.1)

        self.pi.i2c_write_byte_data( self.i2c_comp, 0x4b, 0x01 )
        time.sleep(0.1)

        self.pi.i2c_write_byte_data( self.i2c_comp, 0x4c, 0x00 )
        time.sleep(0.1)
        self.pi.i2c_write_byte_data( self.i2c_comp, 0x4e, 0x84 )
        time.sleep(0.1)
        self.pi.i2c_write_byte_data( self.i2c_comp, 0x51, 0x04 )
        time.sleep(0.1)
        self.pi.i2c_write_byte_data( self.i2c_comp, 0x52, 0x16 )

        time.sleep(0.3)

    def read_accel( self ):
        x_l = self.pi.i2c_read_byte_data( self.i2c_accel, 0x02 )
        x_m = self.pi.i2c_read_byte_data( self.i2c_accel, 0x03 )
        y_l = self.pi.i2c_read_byte_data( self.i2c_accel, 0x04 )
        y_m = self.pi.i2c_read_byte_data( self.i2c_accel, 0x05 )
        z_l = self.pi.i2c_read_byte_data( self.i2c_accel, 0x06 )
        z_m = self.pi.i2c_read_byte_data( self.i2c_accel, 0x07 )

        x = ( ( x_m * 256 ) + ( x_l & 0xf0 ) ) / 16
        if ( x > 2047 ):
            x = x - 4096
        y = ( ( y_m * 256 ) + ( y_l & 0xf0 ) ) / 16
        if ( y > 2047 ):
            y = y - 4096
        z = ( ( z_m * 256 ) + ( z_l & 0xf0 ) ) / 16
        if ( z > 2047 ):
            z = z - 4096

        return ( x, y, z )


    def read_magnet( self ):
        x_l = self.pi.i2c_read_byte_data( self.i2c_comp, 0x42 )
        x_m = self.pi.i2c_read_byte_data( self.i2c_comp, 0x43 )
        y_l = self.pi.i2c_read_byte_data( self.i2c_comp, 0x44 )
        y_m = self.pi.i2c_read_byte_data( self.i2c_comp, 0x45 )
        z_l = self.pi.i2c_read_byte_data( self.i2c_comp, 0x46 )
        z_m = self.pi.i2c_read_byte_data( self.i2c_comp, 0x47 )
        t_l = self.pi.i2c_read_byte_data( self.i2c_comp, 0x48 )
        t_m = self.pi.i2c_read_byte_data( self.i2c_comp, 0x49 )

        x = ( x_m <<5 ) + ( x_l >>3 )
        if ( x > 4095 ):
            x = x - 8192
        y = ( y_m <<5 ) + ( y_l >>3 )
        if ( y > 4095 ):
            y = y - 8192
        z = ( z_m <<7 ) + ( z_l >>1 )
        if ( z > 16383 ):
            z = z - 32768

        return ( x, y, z )

    def read_gyro( self ):
        x_l = self.pi.i2c_read_byte_data( self.i2c_gyro, 0x02 )
        x_m = self.pi.i2c_read_byte_data( self.i2c_gyro, 0x03 )
        y_l = self.pi.i2c_read_byte_data( self.i2c_gyro, 0x04 )
        y_m = self.pi.i2c_read_byte_data( self.i2c_gyro, 0x05 )
        z_l = self.pi.i2c_read_byte_data( self.i2c_gyro, 0x06 )
        z_m = self.pi.i2c_read_byte_data( self.i2c_gyro, 0x07 )

        x = ( x_m * 256 ) + x_l
        if ( x > 32767 ):
            x = x - 65536
        y = ( y_m * 256 ) + y_l
        if ( y > 32767 ):
            y = y - 65536
        z = ( z_m * 256 ) + z_l
        if ( z > 32767 ):
            z = z - 65536

        return ( x, y, z )

    def get_compass( self ):
        ( x, y, z ) = self.read_magnet( )
        x = x - self.calib_x 
        y = y - self.calib_y

        rad = math.atan2( x, y )
        deg = math.degrees( rad )
        return( deg * -1 )

    def get_compass_360( self ):
        deg = self.get_compass()
        if ( deg < 0 ):
            deg = deg + 360
        if ( deg == -0 ):
            deg = 0
        return( deg )

    def set_calib( self, x, y ):
        self.calib_x = x
        self.calib_y = y
    
    def get_calib( self ):
        return( self.calib_x, self.calib_y )



