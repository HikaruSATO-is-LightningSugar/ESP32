import pigpio
import time
from mcp4911 import mcp4911

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0

LDAC_PIN = 23
VREF = 3.3

pi = pigpio.pi()

dac = mcp4911( pi, SPI_CE, SPI_SPEED, LDAC_PIN, VREF )

dac.output_volt( 1.5 )


