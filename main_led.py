import machine
import utime
import random


# LEDの初期設定
red    = machine.Pin(13, machine.Pin.OUT)
green  = machine.Pin(12, machine.Pin.OUT)
yellow = machine.Pin(27, machine.Pin.IN)
colors = [red, green, yellow]
color_order = 0
LED_io = True


# スイッチが押された時に割り込み
color_switch_pin = machine.Pin(25, machine.Pin.IN, machine.Pin.PULL_DOWN)
io_switch_pin = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_DOWN)
# 割り込み処理の関数定義
prev_time = 0
def change_color(p):
    global prev_time
    cur_time = utime.ticks_ms()
    if cur_time < prev_time + 150 :
        # 割り込みの感覚が150msec未満だったら
        # チャタリングと判断してスキップ
        return
    print("blue button")
    global color_order
    color_order += 1
def change_LED_io(p):
    global prev_time
    cur_time = utime.ticks_ms()
    if cur_time < prev_time + 150 :
        # 割り込みの感覚が150msec未満だったら
        # チャタリングと判断してスキップ
        return
    print("red button")
    global LED_io
    irq_io = bool(abs(LED_io - 1))
    print(irq_io)
    LED_io = irq_io
color_switch_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=change_color)
io_switch_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=change_LED_io)


# バックグラウンド処理


# mainループ
while True:
    if LED_io:
        led = colors[color_order%3]
        led.value(1)
        utime.sleep(0.15)
        led.value(0)
        utime.sleep(0.15)
    else:
        led.value(0)