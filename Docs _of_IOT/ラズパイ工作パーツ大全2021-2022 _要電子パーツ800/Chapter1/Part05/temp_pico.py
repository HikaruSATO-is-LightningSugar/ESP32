import machine
import time

SENSOR_ADC = 0
VREF = 3.3

mcp9700 = machine.ADC( SENSOR_ADC )

while True:
    value = mcp9700.read_u16()

    volt = value / 65535 * VREF

    temp = volt * 100 - 50

    print ( "Temperature:", temp, "C" )
    
    time.sleep( 1 )


