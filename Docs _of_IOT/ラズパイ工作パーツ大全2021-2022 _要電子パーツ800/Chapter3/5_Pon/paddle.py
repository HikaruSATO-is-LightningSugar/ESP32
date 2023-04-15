import Adafruit_SSD1306
import time
import pigpio
from mcp3002 import mcp3002
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

RST = None
I2C_ADDR = 0x3c

SW_PIN = 23

font_path = "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf"
font_size = 8
font_size_m = 12
font_size_t = 16

display_x = 128
display_y = 64

score_title_co = ( 0, 56 )
score_co = ( 30, 56 )
score_fill = ( 30, 56 , 79, 63 )
level_up_score = 5

paddle_size = 30
paddle_thin = 2
paddle_y = 50
paddle_shave = 2
paddle_min = 4

ball_size = 2
ball_speed = 2

wall_top = 0
wall_left = 0
wall_right = display_x - ball_size + 1
paddle_hit_y = paddle_y - ball_size + 1

Rx = 10000
SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

pi.set_mode( SW_PIN, pigpio.INPUT )
pi.set_pull_up_down( SW_PIN, pigpio.PUD_DOWN )

adc = mcp3002( pi, SPI_CE, SPI_SPEED, VREF )

def score_write( dh, score ):
    dh.rectangle( score_fill, outline=0, fill=0 )
    dh.text( score_co, str( score ), font=jpfont, fill=255 )

def paddle_write( dh, current, present, size_c, size_p ):
    present_axis = ( present - 1 , paddle_y - 1, present + size_p, paddle_y + paddle_thin )
    current_axis = ( current - 1 , paddle_y - 1, current + size_c, paddle_y + paddle_thin )

    dh.rectangle( present_axis, outline=0, fill=0 )
    dh.rectangle( current_axis, outline=0, fill=1 )

def vol_read( adc, min_x, max_x ):
    value = adc.get_value( READ_CH )
    x = ( max_x - min_x ) / 1023 * value + min_x
    return ( int( x ) )

def ball_write( dh, x, y, xp, yp ):
    present_axis = ( xp - 1, yp - 1, xp + ball_size, yp + ball_size )
    current_axis = ( x - 1, y - 1, x + ball_size, y + ball_size )
    
    dh.rectangle( present_axis, outline=0, fill=0 )
    dh.rectangle( current_axis, outline=0, fill=1 )

def move_ball( xp, yp, dxp, dyp ):
    x = xp + dxp
    y = yp + dyp

    dx = dxp
    dy = dyp
    if ( x <= wall_left - 1 ):
        x = abs( x )
        dx = dxp * -1
    if ( x >= wall_right - 1 ):
        x = 2 * wall_right - x - 1
        dx = dxp * -1
    if ( y <= wall_top ):
        y = abs( y )
        dy = dyp * -1
    if ( y >= paddle_hit_y ):
        dy = dyp * -1

    return ( x, y, dx, dy )

def check_paddle( bx, by, bs, px, ps ):
    check = 0
    if ( by >= paddle_hit_y ):
        if ( px > bx + bs ):
            check = -1
        elif ( bx > px + ps ):
            check = -1
        else:
            check = 1
    return check


def game_play( disp, draw, paddle_size ):
    draw.rectangle( ( 0, 0, display_x, display_y) , outline=0, fill=0 )
    disp.display()

    draw.text( score_title_co, "SCORE:", font=jpfont, fill=255 )
    draw.text( score_co, "0", font=jpfont, fill=255 )
    disp.image(image)
    disp.display()

    paddle_xp = 0
    paddle_x = 0
    paddle_size_p = paddle_size

    paddle_write( draw, paddle_x, paddle_xp, paddle_size, paddle_size_p )

    ball_x = 60
    ball_y = 40

    ball_dx = ball_speed
    ball_dy = ball_speed * -1

    move_min = 0
    move_max = display_x - paddle_size

    score = 0
    flag = 1
    time.sleep( 3 )

    while True:
        ball_xp = ball_x
        ball_yp = ball_y
        ( ball_x, ball_y, ball_dx, ball_dy ) = move_ball( ball_xp, ball_yp, ball_dx, ball_dy )

        ball_write( draw, ball_x, ball_y, ball_xp, ball_yp )

        paddle_xp = paddle_x
        paddle_x = vol_read( adc, move_min, move_max )
        if ( paddle_x != paddle_xp or ball_y >= paddle_hit_y -2 ):
            paddle_write( draw, paddle_x, paddle_xp, paddle_size, paddle_size_p )

        check = check_paddle( ball_x, ball_y, ball_size, paddle_x, paddle_size )

        if ( check == 1 ):
            ball_y = 2 * paddle_hit_y - ball_y - 1
            score = score + 1
            score_write( draw, score )
        elif ( check == -1 ):
            break

        disp.image(image)
        disp.display()

        if ( score % level_up_score == 0 and ball_y == paddle_hit_y ):
            if ( paddle_size > paddle_min ):
                paddle_size_p = paddle_size
                paddle_size = paddle_size - paddle_shave
                paddle_write( draw, paddle_x, paddle_xp, paddle_size, paddle_size_p )
                paddle_size_p = paddle_size
                move_max = display_x - paddle_size

    return 0



disp = Adafruit_SSD1306.SSD1306_128_64( rst=RST, i2c_address=I2C_ADDR )

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new( '1', ( width, height ) )

draw = ImageDraw.Draw( image )
jpfont = ImageFont.truetype(font_path, font_size, encoding='unic')
jpfont_t = ImageFont.truetype(font_path, font_size_t, encoding='unic')
jpfont_m = ImageFont.truetype(font_path, font_size_m, encoding='unic')

while True:
    draw.text( ( 8, 30 ), "ボタンを押してスタート", font=jpfont_m, fill=255 )
    disp.image( image )
    disp.display()   

    while ( pi.read( SW_PIN ) == pigpio.LOW ):
        time.sleep( 0.1 )

    game_play( disp, draw, paddle_size )

    draw.text( ( 15, 20 ), "GAME OVER", font=jpfont_t, fill=255 )
    disp.image( image )
    disp.display()

    time.sleep( 5 )

    draw.rectangle( ( 0, 0, display_x, display_y) , outline=0, fill=0 )
    disp.display()




