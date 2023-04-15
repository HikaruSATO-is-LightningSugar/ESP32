import pigpio
from l3gd20h import l3gd20h
import time

range = 0

l3gd20h_addr = 0x6b
i2c_channel = 1

pi = pigpio.pi()

gyro = l3gd20h( pi, i2c_channel, l3gd20h_addr, range )

while True:
    ( x, y, z ) = gyro.get_dps()
    print ( "X:{:.2f}dps  Y:{:.2f}dps  Z:{:.2f}dps".format( x, y, z ) ) 

    time.sleep( 0.5 )

