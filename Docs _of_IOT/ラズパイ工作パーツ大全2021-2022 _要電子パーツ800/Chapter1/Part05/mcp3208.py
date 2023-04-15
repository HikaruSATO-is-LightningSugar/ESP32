import pigpio

class mcp3208:
    def __init__( self, gpio, ss, speed, vref ):
        self.ss = ss
        self.speed = speed
        self.vref = vref
        self.pi = gpio
        
        self.adc_h = self.pi.spi_open( self.ss, self.speed, 0 )
        
    def get_value( self, ch ):
        cmd_h = 0b110 | ( ch >> 2 )
        cmd_l = ( ch & 0b11 ) << 6
        ( c, raw ) = self.pi.spi_xfer( self.adc_h, [ cmd_h , cmd_l , 0 ])
        value =  ( raw[1] & 0x0f ) <<8 | raw[2]
        return value

    def get_volt( self, value ):
        return value * self.vref / float( 4095 )

