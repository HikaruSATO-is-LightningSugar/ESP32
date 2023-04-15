import pigpio
import time
from mcp3002 import mcp3002

TH = 1.0

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

adc = mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

while True:
    volt = adc.get_volt( READ_CH )

    if ( volt > TH ):
        print( "Wet  Volt:{:.2f}V".format( volt ) )
    else:
        print( "Dry  Volt:{:.2f}V".format( volt ) )

    time.sleep( 1 )


