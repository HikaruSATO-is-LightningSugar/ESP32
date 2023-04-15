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
    result = ""
    ch = 0
    while ( ch < cds_number ):
        volt = adc.get_volt( ch )
        if ( volt != 0 ):
            cds_r = ( Ve - volt ) / volt * Rx / 1000
            result = result + "CH{}:{:.2f}k ".format( ch, cds_r )
        else:
            result = result + "CH{}:--- ".format( ch )
        ch = ch + 1

    print( result )

    time.sleep( 1 )


