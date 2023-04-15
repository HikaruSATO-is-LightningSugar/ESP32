import pigpio
import time

class sht31:
	def __init__( self, pi, ch, addr ):
		self.pi = pi
		self.ch = ch
		self.addr = addr
		self.i2c = self.pi.i2c_open( self.ch, self.addr )
		time.sleep(1)

	def read_sensor( self ):
		self.pi.i2c_write_byte_data( self.i2c, 0x02c, 0x06 )
		time.sleep( 0.1 )
		( count, value ) = self.pi.i2c_read_i2c_block_data( self.i2c, 0x00, 6 )

		temp_buf = value[ 0 ] << 8 | value[ 1 ]
		temp = -45 + ( 175 * temp_buf / 65535.0 )

		humi_buf = value[3] << 8 | value[4]
		humi = humi_buf * 100 / 65535.0

		return( round( temp, 3 ), round( humi, 2 ) )
