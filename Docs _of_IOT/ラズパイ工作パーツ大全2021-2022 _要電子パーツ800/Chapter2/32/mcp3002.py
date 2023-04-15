import pigpio

class mcp3002:
    def __init__( self, handle, ss, speed, vref ):
        self.ss = ss
        self.speed = speed
        self.vref = vref
        self.pi = handle
        
        self.spi = self.pi.spi_open( self.ss, self.speed )
                
    def get_value( self, ch ):
        command = 0x68 | ( 0x18 * ch ) 
        ( count, data ) = self.pi.spi_xfer( self.spi, [ command, 0x00  ] )

        value = ( data[0] << 8 | data[1] ) & 0x3ff
        return value

    def calc_volt( self, value ):
        return value * self.vref / float( 1023 )

    def get_volt( self, ch ):
        value = self.get_value( ch )
        volt = self.calc_volt( value )
        return volt

