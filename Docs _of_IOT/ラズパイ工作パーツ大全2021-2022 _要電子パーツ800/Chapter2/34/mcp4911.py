import pigpio
import time

class mcp4911:
    def __init__( self, handle, ss, speed, ldac, vref ):
        self.ss = ss
        self.speed = speed
        self.pi = handle
        self.ldac = ldac
        self.vref = vref
        self.div = 1023

        self.spi = self.pi.spi_open( self.ss, self.speed )

        self.pi.set_mode( self.ldac, pigpio.OUTPUT )
        self.pi.write( self.ldac, pigpio.HIGH )

    def output_value( self, value ):
        self.pi.write( self.ldac, pigpio.HIGH )
        time.sleep( 0.01 )

        value = int( value )
        if ( value < 0 ):
            value = 0
        if ( value > 1023 ):
            value = 1023

        cmd1 = ( 0b0011 << 4 ) | ( value >> 6 )
        cmd2 = ( value << 2 ) & 0xff
        ( count, data ) = self.pi.spi_xfer( self.spi, [ cmd1, cmd2 ] )

        print ( bin(cmd1), bin(cmd2) )

        time.sleep( 0.1 )
        self.pi.write( self.ldac, pigpio.LOW )
    
    def output_volt( self, volt ):
        value = volt / self.vref * 1023
        self.output_value( value )
        

