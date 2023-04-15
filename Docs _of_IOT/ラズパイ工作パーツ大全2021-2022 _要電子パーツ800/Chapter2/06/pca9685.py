import pigpio
import time

class pca9685:
	def __init__( self, pi_h, addr ):
		self.pi = pi_h
		self.addr = addr
		
		self.drv_h = self.pi.i2c_open( 1, self.addr )
		self.pi.i2c_write_byte_data( self.drv_h, 0x00, 0x21 )

	def set_freq( self, freq ):
		self.freq = freq

		osc_clock = 25 * 1000 * 1000
		prescale = int ( osc_clock / ( 4096.0 * self.freq ) - 1 )
		
		oldreg = self.pi.i2c_read_byte_data( self.drv_h, 0x00 )
		newreg = ( oldreg & 0x7f ) | 0x10

		self.pi.i2c_write_byte_data( self.drv_h, 0x00, newreg )
		self.pi.i2c_write_byte_data( self.drv_h, 0xfe, prescale )
		self.pi.i2c_write_byte_data( self.drv_h, 0x00, oldreg )

		time.sleep( 0.01 )
		
	def set_pulse( self, ch, pulse ):
		p = int( pulse )
		if ( p > 4095 or p < 0 ):
			return ( -1 )
		else:
			reg_on_l = ( ch * 4 ) + 6
			reg_on_h = ( ch * 4 ) + 7
			reg_off_l = ( ch * 4 ) + 8
			reg_off_h = ( ch * 4 ) + 9
		
			val_l = p & 0xff
			val_h = p >> 8
		
			self.pi.i2c_write_byte_data( self.drv_h, reg_on_l, 0x00 )
			self.pi.i2c_write_byte_data( self.drv_h, reg_on_h, 0x00 )
		
			self.pi.i2c_write_byte_data( self.drv_h, reg_off_l, val_l )
			self.pi.i2c_write_byte_data( self.drv_h, reg_off_h, val_h )
		
			return ( 1 )

	def set_pulse_t( self, ch, pulse ):
		max_width = 1000.0 * 1000.0 / self.freq
		width = int ( 4095 * pulse / max_width )
		self.set_pulse( ch, width )
