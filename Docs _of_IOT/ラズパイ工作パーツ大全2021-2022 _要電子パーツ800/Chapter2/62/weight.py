import pigpio
import time
from HX711 import sensor

DATA_PIN = 23
CLOCK_PIN = 24
TARE_PIN = 25

TARE_TIMES = 10
MEASURE_TIMES = 5

RATED_VOLT = 0.001
RATED_WEIGHT = 20000

MODE = 1
VDD = 3.3
GAIN = 128
RESO_BIT = 24

pi = pigpio.pi()

pi.set_mode( TARE_PIN, pigpio.INPUT )
pi.set_pull_up_down( TARE_PIN, pigpio.PUD_UP )

tare = 0

ADC = sensor( pi, DATA = DATA_PIN, CLOCK = CLOCK_PIN, mode=MODE )

ADC.start()

while True:
    if( pi.read( TARE_PIN ) == pigpio.LOW ):
        count = 0
        sum = 0
        while ( count < TARE_TIMES ):
            ( c, mode, value ) = ADC.get_reading()
            sum = sum + value
            count = count + 1
            time.sleep( 0.1 )

        tare = sum / TARE_TIMES

        while( pi.read( TARE_PIN ) == pigpio.LOW ):
            time.sleep( 0.1 )
        print( "Tare set. {:.0f}".format( tare ) )

    count = 0
    sum = 0
    while ( count < MEASURE_TIMES ):
        ( c, mode, value ) = ADC.get_reading()
        sum = sum + value
        count = count + 1
        time.sleep( 0.1 )

    value_ave = sum / MEASURE_TIMES
    volt = ( value_ave - tare ) * VDD / ( 2 ** RESO_BIT ) / GAIN
    weight = volt / ( RATED_VOLT * VDD / RATED_WEIGHT )

    print( "Weight : {:.1f}g".format( weight ) )

    time.sleep( 0.5 )


