# -*- coding: utf-8 -*-
from pathlib import Path
from demo_opts import get_device
from luma.core.render import canvas

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

font_path = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
font_size = 18
jpfont = ImageFont.truetype(font_path, font_size, encoding='unic')

device = get_device( )
device.clear()

while True:
    with canvas(device) as draw:
        draw.text( ( 0, 10 ), "ラズパイを", font=jpfont, fill="white" )
        draw.text( ( 25, 34 ), "楽しもう！", font=jpfont, fill="red" )


