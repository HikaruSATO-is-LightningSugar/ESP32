import pigpio

class mcp23017:
	HIGH = 1
	LOW = 1
	PU_OFF = 0
	PU_UP = 1
	OUTPUT = 0
	INPUT = 1
	IODIRA = 0x00
	IODIRB = 0x01
	GPPUA = 0x0c
	GPPUB = 0x0d
	GPIOA = 0x12
	GPIOB = 0x13
	OLATA = 0x14
	OLATB = 0x15
	
	def __init__( self, handle, ch, addr ):
		self.addr = addr
		self.ch = ch
		self.pi = handle
		
		self.i2c = self.pi.i2c_open( self.ch, self.addr )

	def setup( self ):
		self.pi.i2c_write_byte_data( self.i2c, mcp23017.IODIRA, 0xff )
		self.pi.i2c_write_byte_data( self.i2c, mcp23017.IODIRB, 0xff )
		
	def set_mode( self, pin, mode, pu = 1 ):
		if ( pin >= 0 and  pin < 8 ):
			targetdir = mcp23017.IODIRA
			targetpu = mcp23017.GPPUA
		elif ( pin >= 8 and pin < 16 ):
			targetdir = mcp23017.IODIRB
			targetpu = mcp23017.GPPUB
			pin = pin - 8
		else:
			return( -1 )
		
		old_mode = self.pi.i2c_read_byte_data( self.i2c, targetdir )
		old_pu = self.pi.i2c_read_byte_data( self.i2c, targetpu )
		mask = 0x01 << pin

		if ( mode == mcp23017.OUTPUT ):
			new_mode = old_mode & ( ~ mask )
		elif( mode == mcp23017.INPUT ):
			new_mode = old_mode | ( mask )
		
		if ( pu == mcp23017.PU_OFF ):
			new_pu = old_pu & ( ~ mask )
		elif( pu == mcp23017.PU_UP ):
			new_pu = old_pu | ( mask )
		
		self.pi.i2c_write_byte_data( self.i2c, targetdir, new_mode )
		self.pi.i2c_write_byte_data( self.i2c, targetpu, new_pu )
		
		return( 0 )
	
	def read( self, pin ):
		if ( pin >= 0 and  pin < 8 ):
			targetgpio = mcp23017.GPIOA
		elif ( pin >= 8 and pin < 16 ):
			targetgpio = mcp23017.GPIOB
			pin = pin - 8
		else:
			return( -1 )
		
		mask = 0x01 << pin
		st = self.pi.i2c_read_byte_data( self.i2c, targetgpio )
		
		if ( mask & st ):
			return( 1 )
		else:
			return( 0 )

	def write( self, pin, data ):
		if ( pin >= 0 and  pin < 8 ):
			targetotl = mcp23017.OLATA
		elif ( pin >= 8 and pin < 16 ):
			targetotl = mcp23017.OLATB
			pin = pin - 8
		else:
			return( -1 )
		
		mask = 0x01 << pin
		old_st = self.pi.i2c_read_byte_data( self.i2c, targetotl )
		
		if ( data == 0 ):
			new_st = old_st & ( ~ mask )
		elif( data == 1 ):
			new_st = old_st | ( mask )
		
		self.pi.i2c_write_byte_data( self.i2c, targetotl, new_st )
		
		return( 0 )
		
		
		