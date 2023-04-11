# https://micropython-docs-ja.readthedocs.io/ja/latest/library/uasyncio.html

import uasyncio
import machine
import utime

pre_time = utime.ticks_ms()
# MED-PCからの入力を受けたら、3秒割り込み拒否
def MEDPC_callback(p):
    global pre_time
    cur_time = utime.ticks_ms()
    if cur_time < pre_time + 3000:
            return
    else:
        print("SmartCTL input")
        global the_number_of_requests
        the_number_of_requests += 1
        #print('callback function is called!')
    pre_time = cur_time


async def check_dc_nv(dc, period_ms):
    global dc
    while True:
        val = dc.read_uv()
        if val < 190000:
            global the_number_of_requests
            the_number_of_requests += 1
        elif val > 240000:
        await uasyncio.sleep_ms(200)
            
async def main(pin, period_ms):
    dc_pin = machine.Pin(pin, machine.Pin.IN)
    dc = machine.ADC(dc_pin)
    uasyncio.create_task(check_dc_nv(dc, period_ms))
    await uasyncio.sleep_ms(100)