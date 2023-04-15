from machine import Pin, I2C

I2C_SDA = 8
I2C_SCL = 9
I2C_CH = 0

i2c = I2C( I2C_CH, scl=Pin( I2C_SCL ), sda=Pin( I2C_SDA ), freq=100000)
data = i2c.scan()

for buf in data:
    print( hex(buf) )
