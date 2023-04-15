from board import SCL, SDA
import busio
import adafruit_ssd1306
import pigpio
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0

pi = pigpio.pi()

i2c = busio.I2C(SCL, SDA)

disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

font_path = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
font_size = 16

disp.fill( 0 )
disp.show( )

width = disp.width
height = disp.height
image = Image.new( '1', ( width, height ) )

draw = ImageDraw.Draw( image )
jpfont = ImageFont.truetype(font_path, font_size, encoding='unic')

draw.text( ( 0, 10 ), "Raspberry Piで", font=jpfont, fill=1 )
draw.text( ( 0, 30 ), "電子工作をしよう", font=jpfont, fill=1 )

disp.image(image)
disp.show()


