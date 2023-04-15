import pigpio
import time, math
import mcp3002

B = 3435
To = 25
Ro = 10000
R = 10000
E = 3.3

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

adc = mcp3002.mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

while True:
    volt = adc.get_volt( READ_CH )

    Rx = ( ( E - volt ) / volt ) * R
    Xa = math.log( float( Rx ) / float( Ro ) ) / float( B )
    Xb = 1 / ( To + 273 )
    Xb = 1 / ( float( To ) + 273.0 )

    temp = ( 1 / ( Xa + Xb ) ) - 273.0

    print ( "Temperature : {:.2f} C".format( temp ) )

    time.sleep( 0.5 )


