import pigpio

class gp2y0e03:
    def __init__( self, pi, ch, addr ):
        self.pi = pi
        self.ch = ch
        self.addr = addr
        self.i2c = self.i2c = self.pi.i2c_open( self.ch, self.addr )
        
    def read_distance( self ):
        shift = self.pi.i2c_read_byte_data( self.i2c, 0x35 )
        d_h = self.pi.i2c_read_byte_data( self.i2c, 0x5e )
        d_l = self.pi.i2c_read_byte_data( self.i2c, 0x5f )

        d = ( d_h << 4 ) + d_l
        dist = d / ( 16 * pow( 2, shift ) )    
        
        return (dist)
 
