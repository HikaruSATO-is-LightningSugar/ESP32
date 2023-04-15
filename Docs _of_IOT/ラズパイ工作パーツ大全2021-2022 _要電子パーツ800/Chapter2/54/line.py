import pigpio
import time

PREF_PIN = 23

pi = pigpio.pi()

pi.set_mode( PREF_PIN, pigpio.INPUT )
pi.set_pull_up_down( PREF_PIN, pigpio.PUD_OFF )

while True:
    if ( pi.read( PREF_PIN ) == pigpio.HIGH ):
        print ("White")
    else:
        print ("Black")

    time.sleep( 0.5 )
