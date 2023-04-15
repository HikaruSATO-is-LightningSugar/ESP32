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

    print( "X:", x_accel, " Y:", y_accel, " Z:", z_accel )

    time.sleep( 1 )

