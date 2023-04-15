import pigpio

RATIO = 52

LED_PIN = [ 15, 18, 23, 24, 25 ]

pi = pigpio.pi()

for pin in LED_PIN:
    pi.set_mode( pin, pigpio.OUTPUT )
    pi.write( pin, pigpio.LOW )


count = 0
for pin in LED_PIN:
    if ( count < RATIO // 20 ):
        pi.write( pin, pigpio.HIGH )
    else:
        pi.write( pin, pigpio.LOW )
    count = count + 1

