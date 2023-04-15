import machine
import utime

pin = 12
dc_pin = machine.Pin(pin, machine.Pin.IN)
dc = machine.ADC(dc_pin)

while True:
    global dc
    val = dc.read_uv()
    val = val / 1000
    print(str(val) + ' mV')
    utime.sleep(0.1)