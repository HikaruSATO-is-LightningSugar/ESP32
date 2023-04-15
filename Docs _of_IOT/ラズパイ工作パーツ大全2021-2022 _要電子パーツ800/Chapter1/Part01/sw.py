import time
import pigpio

SW_PIN = 18

pi = pigpio.pi()

pi.set_mode( SW_PIN, pigpio.INPUT )

while True:
	if( pi.read( SW_PIN ) == pigpio.HIGH ):
		print("ON.")
	else:
		print("OFF.")

	time.sleep( 1 )


