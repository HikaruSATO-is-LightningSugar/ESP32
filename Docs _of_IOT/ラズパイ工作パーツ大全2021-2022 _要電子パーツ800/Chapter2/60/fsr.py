import pigpio
import time, math
import mcp3002

TH = 2.0

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

adc = mcp3002.mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

while True:
    volt = adc.get_volt( READ_CH )

    if( volt > TH ):
        print ( "Push. Volt: {:.2f} V".format( volt ) )
    else:
        print ( "Release. Volt: {:.2f} V".format( volt ) )

    time.sleep( 0.5 )


