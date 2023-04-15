import pigpio
import time
import mcp3208

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

adc = mcp3208.mcp3208( pi, SPI_CE, SPI_SPEED, VREF )

while True:
    value = adc.get_value( READ_CH )
    volt = value * VREF / 4095.0

    temp = volt * 100 - 50

    print ( "Temperature :", temp, "C" )

    time.sleep( 0.5 )


