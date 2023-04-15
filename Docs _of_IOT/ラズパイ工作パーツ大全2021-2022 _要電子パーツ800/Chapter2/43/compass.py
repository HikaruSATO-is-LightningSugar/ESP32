import pigpio
from bmx055 import bmx055
import time

CALIB_X = 13
CALIB_Y = 9

accel_addr = 0x19
comp_addr = 0x13
gyro_addr = 0x69
I2C_CH = 1

pi = pigpio.pi()

sensor = bmx055( pi, I2C_CH, accel_addr, comp_addr, gyro_addr )

sensor.set_calib( CALIB_X, CALIB_Y )

while True:
    deg = sensor.get_compass_360()

    print ( "Compass : {:.0f}deg".format( deg ) )

    time.sleep( 0.5 )
