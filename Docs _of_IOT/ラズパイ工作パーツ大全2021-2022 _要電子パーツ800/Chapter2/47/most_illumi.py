import pigpio
import time
from mcp3008 import mcp3008

Rx = 10000
Ve = 3.3

cds_number = 8


SPI_CE = 0
SPI_SPEED = 1000000
VREF = 3.3

pi = pigpio.pi()

adc = mcp3008( pi, SPI_CE, SPI_SPEED, VREF )

while True:
    result = 0
    most_r = 1000000
    ch = 0
    while ( ch < cds_number ):
        volt = adc.get_volt( ch )
        if ( volt != 0 ):
            cds_r = ( Ve - volt ) / volt * Rx / 1000
            if ( cds_r < most_r ):
                result = ch
                most_r = cds_r
        ch = ch + 1

    print( "CH{} : {:.2f}kOhm".format( result, most_r ) )

    time.sleep( 1 )


