import time
import pigpio

SW_PIN = 12

pi = pigpio.pi()

pi.set_mode( SW_PIN, pigpio.INPUT )
pi.set_pull_up_down( SW_PIN, pigpio.PUD_DOWN )

while True:
	if( pi.read( SW_PIN ) == pigpio.HIGH ):
		print("On.")
	else:
		print("Off.")

	time.sleep( 1 )


