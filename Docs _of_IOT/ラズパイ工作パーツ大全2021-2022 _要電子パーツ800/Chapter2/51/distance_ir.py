import pigpio
import time
from gp2y0e03 import gp2y0e03

GP2Y0E03_ADDR = 0x40

I2C_CH = 1

pi = pigpio.pi()

ir_sensor = gp2y0e03( pi, I2C_CH, GP2Y0E03_ADDR )

time.sleep(1)

while True:
    distance = round( ir_sensor.read_distance(), 1)

    print ( "Distance: {:.1f} cm".format( distance ) )

    time.sleep(1)
