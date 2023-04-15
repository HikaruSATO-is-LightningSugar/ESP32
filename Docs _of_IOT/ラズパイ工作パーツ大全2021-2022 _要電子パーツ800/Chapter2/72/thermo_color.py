import adafruit_amg88xx
import busio, board
import time, sys
import pygame
from pygame.locals import *
from temp_color import temp_color

SENSOR_ADDR = 0x68

COL_NUM = 8
ROW_NUM = 8

BOX_SIZE = 30
COLOR_MAX = 255
TEMP_MAX = 30

i2c = busio.I2C(board.SCL, board.SDA)

sensor = adafruit_amg88xx.AMG88XX( i2c, addr = SENSOR_ADDR )
tc = temp_color( )

pygame.init()
screen = pygame.display.set_mode( ( BOX_SIZE * COL_NUM , BOX_SIZE * ROW_NUM ) )
pygame.display.set_caption("Thermograph")

screen.fill( ( 255, 255, 255 ) )
pygame.display.update()


while True:
    data = sensor.pixels

    row = 0
    while ( row < ROW_NUM ):
        col = 0
        while ( col < COL_NUM ):
            val = data[row][col]
            ( r, g, b ) = tc.temp_to_color( val )
            
            box = ( col * BOX_SIZE, row * BOX_SIZE, (col + 1) * BOX_SIZE - 1, ( row + 1 ) * BOX_SIZE - 1)
            pygame.draw.rect( screen, ( r, g, b ), Rect( box ) )

            col = col + 1
        row = row + 1

    pygame.display.update()

    time.sleep( 0.1 )

    for event in pygame.event.get():
        if( event.type == QUIT ):
            pygame.quit()
            sys.exit()
