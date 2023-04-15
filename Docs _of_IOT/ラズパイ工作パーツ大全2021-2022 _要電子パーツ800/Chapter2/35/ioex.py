import pigpio
import time
from mcp23017 import mcp23017

MCP23017_ADDR = 0x20
I2C_CH = 1

OUT_PIN = 8
IN_PIN = 7

pi = pigpio.pi()

ioex = mcp23017( pi, I2C_CH, MCP23017_ADDR )
ioex.setup()

ioex.set_mode( OUT_PIN , mcp23017.OUTPUT ) 
ioex.set_mode( IN_PIN , mcp23017.INPUT, mcp23017.PU_UP )

while( True ):
    ioex.write( OUT_PIN, pigpio.HIGH )
    time.sleep(0.5)
    ioex.write( OUT_PIN, pigpio.LOW )
    time.sleep(0.5)

    if ( ioex.read( IN_PIN ) == pigpio.HIGH ):
        print( "ON." )
    else:
        print( "OFF." )
