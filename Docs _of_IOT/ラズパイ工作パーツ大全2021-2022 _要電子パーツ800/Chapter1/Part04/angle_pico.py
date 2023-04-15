from machine import Pin, I2C
import time
from mma8452_pico import mma8452

I2C_SDA = 8
I2C_SCL = 9
I2C_CH = 0

MMA8452_ADDR = 0x1d
MMA8452_RANGE = 2

i2c = I2C( I2C_CH, scl=Pin( I2C_SCL ), sda=Pin( I2C_SDA ), freq=100000)
i2c.scan()

sensor = mma8452( i2c, MMA8452_ADDR )
sensor.begin( MMA8452_RANGE )

while True:
    ( x_accel, y_accel, z_accel ) = sensor.get_accel()
    ( angle_x, angle_y ) = sensor.conv_angle( x_accel, y_accel, z_accel )

    print( "Angle X:", angle_x, " Y:", angle_y )

    time.sleep( 1 )

