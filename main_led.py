import machine
import utime
import random


# LEDの初期設定
red    = machine.Pin(15, machine.Pin.OUT)
green  = machine.Pin(2, machine.Pin.OUT)
yellow = machine.Pin(4, machine.Pin.IN)
colors = [red, green, yellow]
color_order = 0
LED_io = True


# スイッチが押された時に割り込み
color_switch_pin = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)
io_switch_pin = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_DOWN)
alter_switch_pin = machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_DOWN)
# 割り込み処理の関数定義
pre_time = utime.ticks_ms()
blue_times = 0
red_times = 0

def change_color(p):
    global pre_time
    cur_time = utime.ticks_ms()
    # 割り込みの感覚が200msec未満だったら
    # チャタリングと判断してスキップ
    if cur_time < pre_time + 200 :
        return
    else:
        global blue_times
        blue_times += 1
        print(blue_times)
        print("blue button")
        global color_order
        color_order += 1
    pre_time = cur_time
    
def change_LED_io(p):
    global pre_time
    cur_time = utime.ticks_ms()
    # 割り込みの感覚が200msec未満だったら
    # チャタリングと判断してスキップ
    if cur_time < pre_time + 200 :
        return
    else:
        global red_times
        red_times += 1
        print(red_times)
        print("red button")
        global LED_io
        #irq_io = bool(abs(LED_io - 1))
        #print(irq_io)
        LED_io = bool(abs(LED_io - 1))
    pre_time = cur_time
        
def chattering_timer(p):
    global pre_time
    global blue_times
    blue_times += 1
    cur_time = utime.ticks_ms()
    timedelta = cur_time - pre_time
    if timedelta > 200 :
        print('\n')
    output_str = str(blue_times) + " button:\t" +  str(timedelta) + ' \t(ms)'
    print(output_str)
    pre_time = cur_time
    
    

color_switch_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=chattering_timer)
io_switch_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=chattering_timer)
alter_switch_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=chattering_timer)


# バックグラウンド処理


# mainループ
while True:
    if LED_io:
        led = colors[color_order%3]
        led.value(1)
        utime.sleep(0.1)
        led.value(0)
        color_order += 1
        
    else:
        led.value(0)

