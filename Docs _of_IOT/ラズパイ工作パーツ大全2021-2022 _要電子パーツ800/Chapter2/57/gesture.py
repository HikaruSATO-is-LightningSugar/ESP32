from adafruit_apds9960.apds9960 import APDS9960
import busio

SDA_PIN = 2
SCL_PIN = 3

i2c = busio.I2C( SCL_PIN, SDA_PIN )

apds = APDS9960( i2c )
apds.enable_proximity = True
apds.enable_gesture = True

while True:
    gesture = apds.gesture()

    if ( gesture == 1 ):
        print("UP")
    elif ( gesture == 2 ):
        print("DOWN")
    elif ( gesture == 3 ):
        print("LEFT")
    elif ( gesture == 4 ):
        print("RIGHT")
