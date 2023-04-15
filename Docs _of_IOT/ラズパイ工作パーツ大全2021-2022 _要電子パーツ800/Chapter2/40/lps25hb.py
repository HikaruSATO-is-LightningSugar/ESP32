import pigpio
import time

class lps25hb:
	def __init__( self, pi, ch, addr ):
		self.pi = pi
		self.ch = ch
		self.addr = addr
		self.i2c = self.pi.i2c_open( self.ch, self.addr )

		self.pi.i2c_write_byte_data( self.i2c, 0x21, 0x04 )
		time.sleep( 0.1 )
		self.pi.i2c_write_byte_data( self.i2c, 0x21, 0x80 )
		time.sleep( 0.1 )
		self.pi.i2c_write_byte_data( self.i2c, 0x20, 0x92 )
		time.sleep( 0.1 )

	def get_press( self ):
		pxl = self.pi.i2c_read_byte_data( self.i2c, 0x28 )
		pl = self.pi.i2c_read_byte_data( self.i2c, 0x29 )
		ph = self.pi.i2c_read_byte_data( self.i2c, 0x2a )

		value = ( ph <<16 ) | ( pl <<8 ) | pxl

		press = value / 4096

		return( press )

	def get_temp( self ):
		tl = self.pi.i2c_read_byte_data( self.i2c, 0x2b )
		th = self.pi.i2c_read_byte_data( self.i2c, 0x2c )

		value = ( th <<8 ) | tl

		print ("{:x}".format(value)) 

		if ( value > 0x7fff ):
			value = value - 0xffff

		temp = value / 480 + 42.5

		return( temp )
