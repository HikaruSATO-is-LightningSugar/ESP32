# https://micropython-docs-ja.readthedocs.io/ja/latest/library/uasyncio.html

import uasyncio
import machine

async def blink(led, period_ms):
    while True:
        led.on()
        await uasyncio.sleep_ms(5)
        led.off()
        await uasyncio.sleep_ms(period_ms)

async def main(led1, led2):
    uasyncio.create_task(blink(led1, 700))
    uasyncio.create_task(blink(led2, 400))
    await uasyncio.sleep_ms(10_000)


# 一般的なボードでの実行
from machine import Pin
uasyncio.run(main(Pin(1), Pin(2)))



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