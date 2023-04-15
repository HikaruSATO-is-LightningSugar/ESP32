import time
import pigpio

IN_PIN = [ 12, 16, 20, 21 ]
SEL_PIN = [ 23, 24, 25 ]

KEY_MAP = [ [ '.', '7', '4', '1' ], 
            [ '0', '8', '5', '2' ],
            [ '\n','9', '6', '3' ] ]

pi = pigpio.pi()

i = 0
while ( i < len( SEL_PIN ) ):
	pi.set_mode( SEL_PIN[i], pigpio.OUTPUT )
	pi.write( SEL_PIN[i], pigpio.HIGH )
	i = i + 1

i = 0
while ( i < len( IN_PIN ) ):
	pi.set_mode( IN_PIN[i], pigpio.INPUT )
	pi.set_pull_up_down( IN_PIN[i], pigpio.PUD_OFF )
	i = i + 1

keybuf = []

def keypad():
	global keybuf
	fg_in = 0
	i = 0
	while( i < len( SEL_PIN ) ):
		pi.write( SEL_PIN[ i ], pigpio.LOW )
		j = 0
		while( j < len( IN_PIN ) ):
			if ( pi.read( IN_PIN[ j ] ) == pigpio.LOW ):
				keybuf.append( KEY_MAP[i][j] )
				fg_in = 1
				while ( pi.read( IN_PIN[ j ] ) == pigpio.LOW ) :
					time.sleep( 0.05 )
			j = j + 1
		pi.write( SEL_PIN[ i ], pigpio.HIGH )
		i = i + 1
	return ( fg_in )

def bufread():
	global keybuf
	buf = ''
	i = 0
	point = 0
	while ( i < len( keybuf ) ):
		if ( keybuf[i] == '\n' ):
			break
		elif( keybuf[i] == '.' ):
			point = point + 1
			if ( point > 1 ):
				break
			else:
				buf = buf + keybuf[i]
		else:
			buf = buf + keybuf[i]
		i = i + 1
	
	keybuf = []
	return ( float( buf ) )

while ( True ):
	f = keypad()
	if ( f == 1 ):
		if( keybuf.count('\n') > 0 ):
			value = bufread()
			print( value )

