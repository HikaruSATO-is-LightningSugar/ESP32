import pigpio
import time

class vcnl4010:
	def __init__( self, pi, ch, addr ):
		self.pi = pi
		self.ch = ch
		self.addr = addr
		self.i2c = self.pi.i2c_open( self.ch, self.addr )
		time.sleep(1)

		self.set_LEDcurrent( 200 )

	def set_LEDcurrent( self, current = 200 ):
		current = int( current / 10 )
		if ( current > 20 ):
			current = 20
		elif( current < 0 ):
			current = 0

		self.pi.i2c_write_byte_data( self.i2c, 0x83, current )


	def read_proximity( self ):
		instat = self.pi.i2c_read_byte_data( self.i2c, 0x8e )
		self.pi.i2c_write_byte_data( self.i2c, 0x8e, instat )

		self.pi.i2c_write_byte_data( self.i2c, 0x80, 0x08 )
		while True:
			status = self.pi.i2c_read_byte_data( self.i2c, 0x80 )
			if( status & 0x20 ):
				hb = self.pi.i2c_read_byte_data( self.i2c, 0x87 )
				lb = self.pi.i2c_read_byte_data( self.i2c, 0x87 )
				value = hb << 8 | lb
				break

		return( value )

