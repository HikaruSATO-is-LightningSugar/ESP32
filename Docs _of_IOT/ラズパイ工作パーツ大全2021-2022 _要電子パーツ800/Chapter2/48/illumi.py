import adafruit_vcnl4040
import time
import board, busio

i2c = busio.I2C( board.SCL, board.SDA )
sensor = adafruit_vcnl4040.VCNL4040( i2c )

while True:
    illumi = sensor.lux

    print( "Illuminance : {:.0f} lx".format( illumi ) )

    time.sleep( 0.5 )
