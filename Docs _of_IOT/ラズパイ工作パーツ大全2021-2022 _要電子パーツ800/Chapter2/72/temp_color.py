import math

class temp_color:
    def __init__( self, temp_min = 0, temp_max = 40, gain = 10, x_set = 0 , green_set = 0.6, color_val_max = 255 ):
        self.gain = gain
        self.x_set = x_set
        self.green_set = green_set

        self.temp_min = temp_min
        self.temp_max = temp_max
        self.color_val_max = color_val_max

    def calc_sigmoid( self, val, of ):
        ans = ( math.tanh( ( val + of ) * self.gain /2 ) + 1 ) / 2
        return( ans )

    def color_ratio( self, val ):
        val = ( val * 2 ) - 1
        r = self.calc_sigmoid( val, self.x_set * -1 )
        g = self.calc_sigmoid( val, self.green_set ) - self.calc_sigmoid( val, self.green_set * -1 )
        b = 1 - self.calc_sigmoid( val, self.x_set )

        return( r, g, b )

    def temp_to_color( self, temp ):
        if ( temp < self.temp_min ):
             temp = self.temp_min
        if ( temp > self.temp_max ):
             temp = self.temp_max

        val = ( temp - self.temp_min ) / ( self.temp_max - self.temp_min )
#        print( val )

        ( r, g, b ) = self.color_ratio( val )

        red = int( r * self.color_val_max )
        green = int( g * self.color_val_max )
        blue = int( b * self.color_val_max )

        return( red, green, blue )
