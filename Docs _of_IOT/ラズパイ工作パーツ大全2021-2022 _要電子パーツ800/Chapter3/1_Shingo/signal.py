import pigpio
import time
import pygame.mixer

ROAD_GREEN_PIN = 14
ROAD_YELLOW_PIN = 15
ROAD_RED_PIN = 18

CROSS_RED_PIN = 23
CROSS_GREEN_PIN = 24

CROSS_SOUND = "cross.mp3"

ROAD_GREEN_TIME = 15
ROAD_YELLOW_TIME = 3

CROSS_GREEN_TIME = 15
CROSS_FLUSH_COUNT = 5
CROSS_FLUSH_INTERVAL = 0.5

ALL_RED_TIME = 2

pi = pigpio.pi()

pi.set_mode( ROAD_GREEN_PIN, pigpio.OUTPUT )
pi.set_mode( ROAD_YELLOW_PIN, pigpio.OUTPUT )
pi.set_mode( ROAD_RED_PIN, pigpio.OUTPUT )
pi.set_mode( CROSS_GREEN_PIN, pigpio.OUTPUT )
pi.set_mode( CROSS_RED_PIN, pigpio.OUTPUT )

pi.write( ROAD_GREEN_PIN, pigpio.LOW )
pi.write( ROAD_YELLOW_PIN, pigpio.LOW )
pi.write( ROAD_RED_PIN, pigpio.HIGH )
pi.write( CROSS_GREEN_PIN, pigpio.LOW )
pi.write( CROSS_RED_PIN, pigpio.HIGH )

pygame.mixer.init()

while True:
    pi.write( ROAD_GREEN_PIN, pigpio.HIGH )
    pi.write( ROAD_RED_PIN, pigpio.LOW )
    time.sleep( ROAD_GREEN_TIME )

    pi.write( ROAD_GREEN_PIN, pigpio.LOW )
    pi.write( ROAD_YELLOW_PIN, pigpio.HIGH )
    time.sleep( ROAD_YELLOW_TIME )

    pi.write( ROAD_YELLOW_PIN, pigpio.LOW )
    pi.write( ROAD_RED_PIN, pigpio.HIGH )
    time.sleep( ALL_RED_TIME )

    pi.write( CROSS_RED_PIN, pigpio.LOW )
    pi.write( CROSS_GREEN_PIN, pigpio.HIGH )

    pygame.mixer.music.load( CROSS_SOUND )
    pygame.mixer.music.play( -1, 0.0 )
    time.sleep( CROSS_GREEN_TIME )

    pygame.mixer.music.stop( )

    i = 0
    while( i < CROSS_FLUSH_COUNT ):
        pi.write( CROSS_GREEN_PIN, pigpio.LOW )
        time.sleep( CROSS_FLUSH_INTERVAL )

        pi.write( CROSS_GREEN_PIN, pigpio.HIGH )
        time.sleep( CROSS_FLUSH_INTERVAL )

        i = i + 1

    pi.write( CROSS_GREEN_PIN, pigpio.LOW )
    pi.write( CROSS_RED_PIN, pigpio.HIGH )
    time.sleep( ALL_RED_TIME )



