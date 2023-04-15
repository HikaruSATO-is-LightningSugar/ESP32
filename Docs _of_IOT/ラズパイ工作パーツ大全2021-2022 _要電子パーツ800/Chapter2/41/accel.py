import pigpio
from lis3dh import lis3dh
import time

range = 2

lis3dh_addr = 0x18
i2c_channel = 1

pi = pigpio.pi()

accel = lis3dh( pi, i2c_channel, lis3dh_addr, range )

while True:
    ( x, y, z ) = accel.read_g()
    print ( "X:{:.2f}G  Y:{:.2f}G  Z:{:.2f}G".format( x, y, z ) ) 

    time.sleep( 0.5 )
