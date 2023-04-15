import pigpio
import time, math

class waterlevel:
    def __init__( self, handle, ch, th ):
        self.h_addr = 0x78
        self.l_addr = 0x77
        self.ch = ch
        self.pi = handle
        self.th = th

        self.gap = 5

        self.level = []
        i = 0
        while ( i < 20 ):
            self.level.append( 0 )
            i = i + 1

        self.i2c_h = self.pi.i2c_open( self.ch, self.h_addr )
        self.i2c_l = self.pi.i2c_open( self.ch, self.l_addr )

    def read_sensor( self ):
        lv = 0
        while ( lv < 8 ):
            self.level[lv] = self.pi.i2c_read_byte_data( self.i2c_l, lv )
            lv = lv + 1
        while ( lv < 20 ):
            self.level[lv] = self.pi.i2c_read_byte_data( self.i2c_h, lv - 8 )
            lv = lv + 1
        
    def get_level( self ):
        self.read_sensor()

        lv = 0
        while ( lv < 20 ):
            if ( self.level[ lv ] > self.th ):
                lv = lv + 1
            else:
                break

        return ( lv * self.gap )


