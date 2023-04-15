import pigpio
import math

class mma8452:
	def __init__( self, pi, ch, addr ):
		self.addr = addr
		self.ch = ch
		self.pi = pi
		self.range = 2
		self.i2c = self.pi.i2c_open( self.ch, self.addr )

	def begin( self, range ):
		self.range = range
		tmp = self.pi.i2c_read_byte_data( self.i2c, 0x2a )
		self.pi.i2c_write_byte_data( self.i2c, 0x2a, tmp & 0xfe )
		
		self.pi.i2c_write_byte_data( self.i2c, 0x0e, range >> 2 )
		
		tmp = self.pi.i2c_read_byte_data( self.i2c, 0x2a )
		self.pi.i2c_write_byte_data( self.i2c, 0x2a, tmp | 0x01 )

	def get_accel( self ):
		x_m = self.pi.i2c_read_byte_data( self.i2c, 0x01 )
		x_l = self.pi.i2c_read_byte_data( self.i2c, 0x02 )
		y_m = self.pi.i2c_read_byte_data( self.i2c, 0x03 )
		y_l = self.pi.i2c_read_byte_data( self.i2c, 0x04 )
		z_m = self.pi.i2c_read_byte_data( self.i2c, 0x05 )
		z_l = self.pi.i2c_read_byte_data( self.i2c, 0x06 )

		x_accel = ( x_m << 4 ) | ( x_l >> 4 )
		if ( x_accel > 2047 ):
			x_accel = x_accel - 4096

		y_accel = ( y_m << 4 ) | ( y_l >> 4 )
		if ( y_accel > 2047 ):
			y_accel = y_accel - 4096

		z_accel = ( z_m << 4 ) | ( z_l >> 4 )
		if ( z_accel > 2047 ):
			z_accel = z_accel - 4096

		return ( - x_accel,  - y_accel,  - z_accel )

	def conv_angle( self, x, y, z ):
		x_angle = math.degrees( math.atan2( x, math.sqrt( y ** 2 + z ** 2 ) ) )
		y_angle = math.degrees( math.atan2( y, math.sqrt( x ** 2 + z ** 2 ) ) )
		return ( x_angle, y_angle )




