import adafruit_amg88xx
import busio, board
import time

SENSOR_ADDR = 0x68

COL_NUM = 8
ROW_NUM = 8

i2c = busio.I2C(board.SCL, board.SDA)

sensor = adafruit_amg88xx.AMG88XX( i2c, addr = SENSOR_ADDR )

while True:
    data = sensor.pixels

    row = 0
    while ( row < ROW_NUM ):
        col = 0
        while ( col < COL_NUM ):
            print( "{: .02f}".format( data[row][col] ), end=" " )
            col = col + 1
        print( "" )
        row = row + 1
    print ("------------------------------------------------")

    time.sleep( 1 )

