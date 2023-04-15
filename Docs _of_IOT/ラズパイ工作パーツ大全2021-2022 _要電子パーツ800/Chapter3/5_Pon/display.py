import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = None
I2C_ADDR = 0x3c

disp = Adafruit_SSD1306.SSD1306_128_64( rst=RST, i2c_address=I2C_ADDR )

font_path = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
font_size = 14
jpfont = ImageFont.truetype(font_path, font_size, encoding='unic')

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new( '1', ( width, height ) )

draw = ImageDraw.Draw( image )

draw.text( ( 25, 20 ), "Raspberry Pi", font=jpfont, fill=1 )

draw.rectangle( ( 20, 50, 110, 60 ) , outline=0, fill=1 )

disp.image(image)
disp.display()



