import pigpio
import time
from mcp3002 import mcp3002

PH_CH = 0

SPI_CE = 0
SPI_SPEED = 1000000
VREF = 3.3

pi = pigpio.pi()

adc = mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

while True:
	ph_value = adc.get_value( PH_CH )
	ph_volt = adc.get_volt( ph_value )

	ph = round( ph_volt * 5.0 / VREF * 3.5 , 1)

	print ( "pH : " , ph )

	time.sleep( 1 )

