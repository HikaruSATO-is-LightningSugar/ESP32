import pigpio
from bmx055 import bmx055
import time

CALIB_X = 0
CALIB_Y = 0

accel_addr = 0x19
comp_addr = 0x13
gyro_addr = 0x69
I2C_CH = 1

pi = pigpio.pi()

sensor = bmx055( pi, I2C_CH, accel_addr, comp_addr, gyro_addr )

sensor.set_calib( CALIB_X, CALIB_Y )

x_max = 0
x_min = 65565
y_max = 0
y_min = 65535


while True:
    ( x, y, z ) = sensor.read_magnet()
    if ( x > x_max ):
        x_max = x
    if ( x < x_min ):
        x_min = x

    if ( y > y_max ):
        y_max = y
    if ( y < y_min ):
        y_min = y

    x_cab = x_max - ( x_max - x_min ) / 2
    y_cab = y_max - ( y_max - y_min ) / 2

    print ( "Calibration  CALIB_X:{:.0f}  CALIB_Y:{:.0f}".format( x_cab, y_cab ) )

    time.sleep( 0.5 )
