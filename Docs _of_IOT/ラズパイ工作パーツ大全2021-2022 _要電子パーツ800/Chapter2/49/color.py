import adafruit_tcs34725
import pigpio
import board, busio
import time

LED = 0

LED_PIN = 23

pi = pigpio.pi()

pi.set_mode( LED_PIN, pigpio.OUTPUT )
pi.write( LED_PIN, pigpio.LOW )

i2c = busio.I2C( board.SCL, board.SDA )

sensor = adafruit_tcs34725.TCS34725( i2c )

pi.write( LED_PIN, LED )

while True:
    ( r, g, b ) = sensor.color_rgb_bytes
    
    print( "Red:{}  Green:{}  Blue:{}".format( r, g, b ) )

    time.sleep( 0.5 )

