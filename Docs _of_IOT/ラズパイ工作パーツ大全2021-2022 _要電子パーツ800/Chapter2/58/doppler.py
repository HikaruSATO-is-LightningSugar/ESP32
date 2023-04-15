import pigpio
import time

serial_tty = "/dev/ttyS0"
serial_speed = 9600

pi = pigpio.pi()

ser = pi.serial_open( serial_tty, serial_speed )

while True:
    try:
        sensor_line = ''
        ( buf_cnt, buf ) = pi.serial_read( ser )
        if ( buf_cnt > 0 ):
            sensor_line = buf.decode()
            sensor_line = sensor_line.replace('\n','')
            sensor_line = sensor_line.replace('\r','')
    
        while( len( sensor_line ) > 1 ):
            cmd = sensor_line[:2]
            sensor_line = sensor_line[2:]
            if ( cmd == '@C' ):
                print( "Approach" )
            elif ( cmd == '@L' ):
                print( "Separation" )
        time.sleep( 0.1 )

    except  KeyboardInterrupt:
        pi.serial_close( ser )
        break



