import pigpio
import time
from mcp3002 import mcp3002

R = 10
E = 3.3

BEND_MIN = 50
BEND_MAX = 650

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

adc = mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

while True:
    volt = adc.get_volt( READ_CH )
    Rx_k = ( E - volt ) / volt * R

    ratio = 1 - ( Rx_k - BEND_MAX ) / ( BEND_MIN - BEND_MAX )
    ratio = round ( ratio * 100 )

    if ( ratio < 0 ):
        ratio = 0
    if ( ratio > 100 ):
        ratio = 100

    print ( "Ratio: {}%  Resistor : {:.0f}kohm".format( ratio, Rx_k )  )

    time.sleep( 1 )


