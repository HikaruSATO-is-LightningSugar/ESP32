import pigpio
import time
from lps25hb import lps25hb

LPS25HB_ADDR = 0x5d

werning_down = 2

interval = 30
compare_time = 10800
mesure_cnt = 10
mesure_interval = 1

waittime = interval - mesure_cnt * mesure_interval

pi = pigpio.pi()
I2C_CH = 1

sensor = lps25hb(pi, I2C_CH, LPS25HB_ADDR )

press_record = []

while ( True ):
    cnt = 0
    val_sum = 0
    while( cnt < mesure_cnt ):
        val_sum = val_sum + sensor.get_press()
        cnt = cnt + 1
        time.sleep( mesure_interval )

    press = val_sum / mesure_cnt
    now_time = time.time()

    press_record.append( [ now_time, press ] )

    while( True ):
        if ( len( press_record ) < 1 ):
            break

        if ( press_record[0][0] + compare_time < now_time ):
            press_record.pop( 0 )
        else:
            break

    i = 0
    press_max = 0
    while ( i < len( press_record ) ):
        if ( press_max < press_record[i][1] ):
            press_max = press_record[i][1]
        i = i + 1

    if ( press_max < press + werning_down ):
        werning = ""
    else:
        werning = "Pressure Dropped.  "

    print( "{}Now Pressure : {:.2f}hPa".format( werning, press ) )

    time.sleep( waittime )


