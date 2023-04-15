import time, math
import pigpio
import mma8452

I2C_CH = 1
MMA8452_ADDR = 0x1d
MMA8452_RANGE = 2

pi = pigpio.pi()

sensor = mma8452.mma8452( pi, I2C_CH, MMA8452_ADDR )
sensor.begin( MMA8452_RANGE )

while True:
    ( x_accel, y_accel, z_accel ) = sensor.get_accel()

    print( "X:", x_accel, " Y:", y_accel, " Z:", z_accel )

    time.sleep( 1 )

