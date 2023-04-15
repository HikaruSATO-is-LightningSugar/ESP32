import time
import pigpio

SW_PIN = 23

pi = pigpio.pi()

pi.set_mode( SW_PIN, pigpio.INPUT )

while True:
	if( pi.read( SW_PIN ) == pigpio.HIGH ):
		print("On.")
	else:
		print("Off.")

	time.sleep( 1 )


