import pigpio
import time
from mcp3002 import mcp3002

Rx = 10000

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

adc = mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

while True:
    volt = adc.get_volt( READ_CH )

    current = volt / Rx
    current_m = current * 1000

    print( "Current : {:.2f} mA".format( current_m ) )

    time.sleep( 1 )


