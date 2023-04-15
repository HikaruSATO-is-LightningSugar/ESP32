import pigpio
from waterlevel import waterlevel
import time

target = 60
th = 70

i2c_channel = 1

pi = pigpio.pi()

wl = waterlevel( pi, i2c_channel, th )

while True:
    level =  wl.get_level()

    if ( level < th ):
        alert = ""
    else:
        alert = "Alert!"

    print( "{} {}cm".format( alert, level ) )

    time.sleep( 0.5 )
