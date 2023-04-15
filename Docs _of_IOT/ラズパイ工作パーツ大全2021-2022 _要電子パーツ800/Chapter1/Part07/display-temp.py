from board import SCL, SDA
import busio
import adafruit_ssd1306
import pigpio
import time
import mcp3208

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

adc = mcp3208.mcp3208( pi, SPI_CE, SPI_SPEED, VREF )

i2c = busio.I2C(SCL, SDA)

disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

font_path = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
font_size = 18

disp.fill( 0 )
disp.show( )

width = disp.width
height = disp.height
image = Image.new( '1', ( width, height ) )

draw = ImageDraw.Draw( image )
jpfont = ImageFont.truetype(font_path, font_size, encoding='unic')

while True:
    value = adc.get_value( READ_CH )
    volt = value * VREF / 4095.0

    temp = volt * 100 - 50

    disp_str = "温度 : {:.2f} 度".format( temp )

    draw.rectangle( (0, 0, width, height), outline=0, fill=0 )
    draw.text( ( 0, 22 ), disp_str, font=jpfont, fill=1 )

    disp.image(image)
    disp.show()

    time.sleep( 1 )


