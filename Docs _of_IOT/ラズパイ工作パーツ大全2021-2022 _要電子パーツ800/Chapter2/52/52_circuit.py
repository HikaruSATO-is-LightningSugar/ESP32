import VL53L1X
import time
import sys
import signal

LASER_ADDR = 0x29
I2C_CH = 1

tof = VL53L1X.VL53L1X( I2C_CH, LASER_ADDR )
tof.open()

tof.start_ranging( 0 )

while True:
    distance = tof.get_distance()
    print( "Distance: {} mm".format( distance ) )
    time.sleep( 1 )


