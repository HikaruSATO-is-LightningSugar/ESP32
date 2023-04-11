# https://micropython-docs-ja.readthedocs.io/ja/latest/library/uasyncio.html
# https://micropython-docs-ja.readthedocs.io/ja/latest/library/machine.ADC.html#machine-adc

import uasyncio
import machine
import utime

adc_pin = machine.Pin(12, machine.Pin.IN)
adc = machine.ADC(adc_pin)

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
    
# MED-PCのSmartCTLを
# SG-231の「28V VDC to TTL ADAPTOR」につないだら、
# なぜか交流電流が流れており、
# TTLの５Vの入力を取り込んで割り込みハンドラーを
# 呼び出すつもりだったのと、
# この入力をタクトスイッチを共有することで、
# 回路として、MED-PC　＝　タクトスイッチON
# の対応を実装するつもりだったのだが、
# 今の所、できそうにない
#
# したがって、応急処置的に、
# 非同期処理として、条件処理をする
# SmartCTLがOFFの時：250.0 ~ 280 mV
# SmartCTLがONの時：160 ~ 190 mV
# の電圧を、ESP32が検出しているので、
# これで、条件処理をして、
# 割り込みハンドラ呼び出しの代わりとする
# 他にもっといい方法があれば、そっちを使うと思う
TTL_pin = 12
async_cycle_ms = 200 
async def check_dc_nv(dc, period_ms):
    global dc
    while True:
        val = dc.read_uv()
        if val < 190000:
            MEDPC_callback()
        elif val > 240000:
        await uasyncio.sleep_ms(period_ms)
            
async def main(pin, period_ms):
    dc_pin = machine.Pin(pin, machine.Pin.IN)
    dc = machine.ADC(dc_pin)
    uasyncio.create_task(check_dc_nv(dc, period_ms))
    await uasyncio.sleep_ms(period_ms)
    
uasyncio.run(main(TTL_pin, async_cycle_ms)