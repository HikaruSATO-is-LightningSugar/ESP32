import pigpio
import time
from lps25hb import lps25hb

LPS25HB_ADDR = 0x5d

pi = pigpio.pi()
I2C_CH = 1

sensor = lps25hb(pi, I2C_CH, LPS25HB_ADDR )

while ( True ):
    press = sensor.get_press()

    print( "Pressure : {:.2f}hPa".format( press ) )

    time.sleep( 0.5 )


