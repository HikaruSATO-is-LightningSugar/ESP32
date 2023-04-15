import pigpio
import time
import mcp3002

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

adc = mcp3002.mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

while True:
    volt = adc.get_volt( READ_CH )

    temp = volt * 100 - 50

    print ( "Temperature : {:.2f} C".format( temp ) )

    time.sleep( 0.5 )


