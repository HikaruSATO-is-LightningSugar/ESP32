from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

SENSOR_ADC = 0
Vdd = 3.3

WIDTH  = 128
HEIGHT = 32

mcp9700 = machine.ADC( SENSOR_ADC )

i2c = I2C( 0 )
oled = SSD1306_I2C( WIDTH, HEIGHT, i2c )

while True:
    value = mcp9700.read_u16()
    volt = value / 65535 * Vdd
    temp = volt * 100 - 50

#    output = "Temp:{:.2f} C".format( temp )

    output = "13.15"

    oled.fill( 0 )
    oled.text( output , 15, 13 )
    oled.show()

    time.sleep( 1 )