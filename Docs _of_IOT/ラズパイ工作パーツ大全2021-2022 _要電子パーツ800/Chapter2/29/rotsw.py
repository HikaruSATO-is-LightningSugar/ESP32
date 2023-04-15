import pigpio
import time

ROT_PIN = [ 14, 15, 23, 24 ]


pi = pigpio.pi()

for i in ROT_PIN:
    pi.set_mode( i, pigpio.INPUT )
    pi.set_pull_up_down( i, pigpio.PUD_DOWN )

data = [ 0, 0, 0, 0 ]

while True:
    i = 0
    while i < len( ROT_PIN ):
        data[i] =pi.read( ROT_PIN[ i ] )
        i = i + 1

    value = data[3] * 8 + data[2] * 4 + data[1] * 2 + data[0]
    print ( "{:} ({:},{:},{:},{:})".format( value, data[3], data[2], data[1], data[0] ) )

    time.sleep( 1 )
