import pigpio
from lis3dh import lis3dh
import time

lis3dh_addr = 0x18
i2c_channel = 1

pi = pigpio.pi()

accel = lis3dh( pi, i2c_channel, lis3dh_addr, range=2 )

while True:
    ( x, y, z ) = accel.read_g()

    ( x_angle, y_angle ) = accel.conv_angle( x, y, z )

    print ( "X Angle:{:.0f}deg  Y Angle:{:.0f}deg".format( x_angle, y_angle ) )

    time.sleep(1)
