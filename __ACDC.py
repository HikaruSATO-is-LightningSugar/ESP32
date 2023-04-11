# https://micropython-docs-ja.readthedocs.io/ja/latest/library/machine.ADC.html#machine-adc

import machine
import utime


 #adc_pin = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
adc_pin = machine.Pin(12, machine.Pin.IN)
adc = machine.ADC(adc_pin)


while True:
    val = adc.read_uv()
    #val = adc.read_u16()
    val = int(val / 1000)
    print(str(val)+' mv')
    utime.sleep(0.17)
    

