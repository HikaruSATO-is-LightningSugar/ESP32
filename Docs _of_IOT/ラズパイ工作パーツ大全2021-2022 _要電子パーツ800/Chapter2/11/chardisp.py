# -*- coding: utf-8 -*-
import pigpio
from aqm0802 import aqm0802
import time

aqm0802_addr = 0x3e
I2C_CH = 1

pi = pigpio.pi()

aqm0802 = aqm0802( pi, I2C_CH, aqm0802_addr )

aqm0802.set_cursol( 0 )
aqm0802.set_blink( 0 )

aqm0802.clear( )
aqm0802.move_home( )
aqm0802.write( u'ラズパイハ' )
aqm0802.move( 2, 1 )
aqm0802.write( u'タノシイヨ!' )

