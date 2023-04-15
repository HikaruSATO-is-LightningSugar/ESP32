import smbus

class GP2:
    __REG_DISTANCE = 0x5E
    __REG_SHIFT = 0x35

    def __init__(self, bus = 1, address = 0x40):
        self.i2c = smbus.SMBus(bus)
        self.addr = address
        self.shift = 2
    
    @property
    def shift(self):
        return self.i2c.read_byte_data(self.addr, self.__REG_SHIFT)
    
    @shift.setter
    def shift(self, sft):
        self.i2c.write_byte_data(self.addr, self.__REG_SHIFT, sft)
    
    @property
    def distance(self):
        try:
            sh = self.shift
            dist = self.i2c.read_i2c_block_data(self.addr, self.__REG_DISTANCE)
        except Exception:
            return -1
        d = ((dist[0] << 4) | dist[1]) / 16 / (2 ** sh)
        if d > (127.8 / sh):
            d = -1 
        return d

    def __del__(self):
        self.i2c.close()
