import pigpio
import time
from mcp3002 import mcp3002

TH = 2.0

HEATER_PIN = 23
SENSOR_PIN = 24

SPI_CE = 0
SPI_SPEED = 1000000
VREF = 3.3
READ_CH = 0

pi = pigpio.pi()

pi.set_mode( HEATER_PIN, pigpio.OUTPUT )
pi.set_mode( SENSOR_PIN, pigpio.OUTPUT )
pi.write( HEATER_PIN, pigpio.LOW )
pi.write( SENSOR_PIN, pigpio.LOW )

adc = mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

while ( True ):
	i = 0
	while ( i < 5 ):
		time.sleep( 0.242 )
		pi.write( HEATER_PIN, pigpio.HIGH )
		time.sleep( 0.008 )
		pi.write( HEATER_PIN, pigpio.LOW )
		i = i + 1
	time.sleep( 0.237 )
	pi.write( SENSOR_PIN, pigpio.HIGH )
	time.sleep( 0.0025 )

	volt = adc.get_volt( READ_CH )
	if( volt < TH ):
		print ( "OK. Volt: {:.2f} V".format( volt ) )
	else:
		print ( "BAD. Volt: {:.2f} V".format( volt ) )

	time.sleep( 0.0025 )
	pi.write( SENSOR_PIN, pigpio.LOW )

	time.sleep( 1 )







