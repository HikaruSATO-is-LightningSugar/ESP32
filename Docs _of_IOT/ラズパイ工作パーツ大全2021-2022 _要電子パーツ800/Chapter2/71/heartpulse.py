from pulse_sensor import pulse_sensor
import pigpio
import time

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3

pi = pigpio.pi()

sensor = pulse_sensor( pi, READ_CH, SPI_CE, SPI_SPEED, VREF )
sensor.startAsyncBPM()

try:
    while True:
        bpm = sensor.BPM
        if( bpm > 0 ):
            print("BPM:", int(bpm) )
        else:
            print("Cannot found pulse.")
        time.sleep(1)
except:
    sensor.stopAsyncBPM()


