import time, math
import mma8452
import pigpio

MMA8452_ADDR = 0x1d
MMA8452_RANGE = 2
I2C_CH = 1

pi = pigpio.pi()

sensor = mma8452.mma8452( pi, I2C_CH, MMA8452_ADDR )
sensor.begin( MMA8452_RANGE )

while True:
    ( x_accel, y_accel, z_accel ) = sensor.get_accel()
    ( angle_x, angle_y ) = sensor.conv_angle( x_accel, y_accel, z_accel )

    print( "Angle X:", angle_x, " Y:", angle_y )

    time.sleep( 1 )

