import board, time
import neopixel
import hsv_to_rgb

STEP = 5
WAIT = 0.05
LED_NUM = 30

pixels = neopixel.NeoPixel( board.D18 , LED_NUM )

hue = 0
strong = 100
value = 100

while True:
	i = 0
	while ( i < LED_NUM ):
		hue_current = hue + STEP * i
		if ( hue_current > 100 ):
			hue_current = hue_current - 1

		( red, green, blue ) = hsv_to_rgb.hsv_to_rgb( hue_current, strong, value )
		pixels[ i ] = ( int( red * 2.55 ), int( green * 2.55 ), int( blue * 2.55 ) )
		i = i + 1

	pixels.show()

	hue = hue + STEP
	if ( hue > 100 ):
		hue = hue - 100
	
	time.sleep( WAIT )








