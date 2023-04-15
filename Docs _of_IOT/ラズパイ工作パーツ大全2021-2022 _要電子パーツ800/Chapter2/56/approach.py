import pigpio
import time
from vcnl4010 import vcnl4010

TH = 4000

VCNL4010_ADDR = 0x13

pi = pigpio.pi()
I2C_CH = 1

sensor = vcnl4010(pi, I2C_CH, VCNL4010_ADDR )

while ( True ):
    value = sensor.read_proximity()

    if( value >= TH ):
        message = "Approach. "
    else:
        message = ""

    print ( "{}Value : {:}".format( message, value ) )

    time.sleep( 0.5 )
