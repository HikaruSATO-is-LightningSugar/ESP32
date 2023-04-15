import pigpio
import time
from sht31 import sht31

SHT31_ADDR = 0x45

pi = pigpio.pi()
I2C_CH = 1

sensor = sht31(pi, I2C_CH, SHT31_ADDR )

while ( True ):
    ( temp, humi ) = sensor.read_sensor()

    thi = 81 / 100 * temp + humi / 100 * ( 99 /100 * temp - 14/.3) + 46.3

    if ( thi > 75 ):
        print( "Hot. THI:{:.0f}".format( thi ) )
    elif( thi < 60 ):
        print( "Cold. THI:{:.0f}".format( thi ) )
    else:
        print( "Comfortable. THI:{:.0f}".format( thi ) )

    time.sleep( 1 )
