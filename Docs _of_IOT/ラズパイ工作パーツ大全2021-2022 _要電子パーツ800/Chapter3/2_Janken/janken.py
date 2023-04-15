import pigpio
import time
import random
import pygame.mixer

GU_PIN = 23
CHOKI_PIN = 24
PA_PIN = 25

HT16K33_ADDR = 0x70

matrix_row = 7
i2c_channel = 1

sound_janken = "janken.mp3"
sound_aiko = "aiko.mp3"
sound_pon = "pon.mp3"
sound_win = "win.mp3"
sound_lose = "lose.mp3"


pattern_gu = [ 0b00000,
               0b00000,
               0b00000,
               0b01110,
               0b11111,
               0b11111,
               0b01110 ]

pattern_choki = [ 0b00010,
                  0b01010,
                  0b01010,
                  0b01010,
                  0b11111,
                  0b11111,
                  0b01110 ]

pattern_pa = [ 0b01100,
               0b01110,
               0b01111,
               0b01111,
               0b11111,
               0b11111,
               0b01110 ]


def matrix_write( pi, pattern ):
    row = 0
    while ( row < matrix_row ):
        pi.i2c_write_byte_data( i2c, row * 2, pattern[row] )
        row = row + 1

def matrix_clear( pi ):
    row = 0
    while ( row < matrix_row ):
        pi.i2c_write_byte_data( i2c, row * 2, 0x00 )
        row = row + 1



pygame.mixer.init()

pi = pigpio.pi()

pi.set_mode( GU_PIN, pigpio.INPUT )
pi.set_mode( CHOKI_PIN, pigpio.INPUT )
pi.set_mode( PA_PIN, pigpio.INPUT )
pi.set_pull_up_down( GU_PIN, pigpio.PUD_DOWN )
pi.set_pull_up_down( CHOKI_PIN, pigpio.PUD_DOWN )
pi.set_pull_up_down( PA_PIN, pigpio.PUD_DOWN )

i2c = pi.i2c_open( i2c_channel, HT16K33_ADDR )

pi.i2c_write_byte_data( i2c, 0x21, 0x01 )
pi.i2c_write_byte_data( i2c, 0x81, 0x01 )
time.sleep(0.1)

random.seed()

aiko = 0

while True:
    matrix_clear( pi )
    com_hand = random.randint( 0, 2 ) 
    
    if ( aiko == 0 ):
        pygame.mixer.music.load( sound_janken )
    else:
        pygame.mixer.music.load( sound_aiko )

    pygame.mixer.music.play( )

    time.sleep( 1 )

    while True:
        gu = pi.read( GU_PIN )
        choki = pi.read( CHOKI_PIN )
        pa = pi.read( PA_PIN )
        if ( gu == pigpio.HIGH or choki == pigpio.HIGH or pa == pigpio.HIGH ):
            time.sleep( 0.2 )
            while( pi.read( GU_PIN ) == pigpio.HIGH or pi.read( CHOKI_PIN ) == pigpio.HIGH or pi.read( PA_PIN ) == pigpio.HIGH ):
                time.sleep( 0.1 )

            break

    if ( gu == pigpio.HIGH ):
        player_hand = 0
    elif ( choki == pigpio.HIGH ):
        player_hand = 1
    else:
        player_hand = 2

    pygame.mixer.music.load( sound_pon )
    pygame.mixer.music.play( )

    if( com_hand == 0 ):
        matrix_write( pi, pattern_gu )
    elif( com_hand == 1 ):
        matrix_write( pi, pattern_choki )
    else:
        matrix_write( pi, pattern_pa )

    time.sleep( 1 )

    if ( com_hand == player_hand ):
       aiko = 1
       time.sleep( 1.5 )
    else:
        break

result = 0

if ( player_hand == 0 and com_hand == 1 ):
    result = 1
if ( player_hand == 1 and com_hand == 3 ):
    result = 1
if ( player_hand == 2 and com_hand == 0 ):
    result = 1

if ( result == 1 ):
    pygame.mixer.music.load( sound_win )
    pygame.mixer.music.play( )
else:
    pygame.mixer.music.load( sound_lose )
    pygame.mixer.music.play( )

time.sleep( 3 )


