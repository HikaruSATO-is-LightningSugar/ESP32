import pigpio

class mcp3008:
    def __init__( self, handle, ss, speed, vref ):
        self.ss = ss
        self.speed = speed
        self.vref = vref
        self.pi = handle
        
        self.spi = self.pi.spi_open( self.ss, self.speed )
                
    def get_value( self, ch ):
        cmd_h = 0b110 | ( ch >> 2 )
        cmd_l = ( ch & 0b11 ) << 6
        ( c, raw ) = self.pi.spi_xfer( self.spi, [ cmd_h , cmd_l , 0 ])
        value =  ( raw[1] & 0x0f ) <<6 | raw[2]
        return value

    def conv_volt( self, value ):
        return value * self.vref / float( 1023 )

    def get_volt( self, ch ):
        value = self.get_value( ch )
        volt = self.conv_volt( value )
        return( volt )
