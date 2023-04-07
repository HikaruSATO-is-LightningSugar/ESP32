#from stepper_arduino import Stepper
from stepper_qiita import Stepper
import time
import utime
import machine


# ステッピングモーターの初期設定
# 参考
# https://github.com/LanghiDev/MicroPython-with-Stepper-motor-28byj-48/blob/master/main.py
# https://qiita.com/kotaproj/items/cd37c971f03fb02c97ce
# 360°＝2048とする
number_of_steps = 2048
# ULN2003 Motor Driver Pins
motor_pin_1 = 25
motor_pin_2 = 26
motor_pin_3 = 27
motor_pin_4 = 13
my_motor =  Stepper(number_of_steps, motor_pin_1, motor_pin_2, motor_pin_3, motor_pin_4)
# モーターの回転速度と、トルクは反比例になってる？？
# set_speed(14) では、LEGOのギアが回らなかった
# おそらく５Vのモーターでは非力なので、シリンジを縮める速度は上限があるようだ。
#
# stepper_arduino.pyを使っていてのエラー
# 途中で止めて（＝ESP32を再起動させて）再度回転さた時と
# テンションがかかりはじめる時とで、
# 逆回転してしまう、、、、なんでだろう
# setSpeed() を10→6に変更して、トルクをあげてみる
my_motor.setSpeed(7)
# 回転数の指定
# 実験1（絹糸、6rpm）：10500μL/510s/60回転　=　80μL/4s/0.5回転
# 実験2（テグス、7rpm）：
rotation = 0.5
# 回転数×360°
angle = rotation * number_of_steps


#  割り込み処理
# MED-PC → SmartCTL →　ESP32でシグナルをもらうときの割り込み処理
# 簡単な処理になるように工夫する！
# 参考
# https://tech-and-investment.com/raspberrypi-pico-12-gpio/
# http://tech-and-investment.com/raspberrypi-pico-14-gpio-interrupt/
# https://micropython-docs-ja.readthedocs.io/ja/latest/esp32/quickref.html
# https://goma483549.hatenablog.com/entry/2021/09/18/104726
SmartCTL_pin = machine.Pin(35, machine.Pin.IN, machine.Pin.PULL_DOWN)
tactswitch_pin = machine.Pin(34, machine.Pin.IN, machine.Pin.PULL_DOWN)
STOPswitch_pin = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_DOWN)
pre_time = utime.ticks_ms()
the_number_of_requests = 0

# 割り込み処理の関数定義
def one_more_syrup(SmartCTL_or_tactswitch):
    global pre_time
    cur_time = utime.ticks_ms()
    # MED-PCからの入力を受けたら、3秒割り込み拒否
    if SmartCTL_or_tactswitch == 'SmartCTL':
        if cur_time < pre_time + 3000:
            return
    # スイッチからの入力を受けたら、チャタリング防止のため0.２秒割り込み拒否
    elif SmartCTL_or_tactswitch == 'tactswitch':
        if cur_time < pre_time + 200:
            return
    else:
        global the_number_of_requests
        the_number_of_requests += 1
        #print('callback function is called!')
    pre_time = cur_time
    
def STOP_motor():
    global pre_time
    cur_time = utime.ticks_ms()
    # スイッチからの入力を受けたら、チャタリング防止のため0.２秒割り込み拒否
    if cur_time < pre_time + 200:
        return
    else:
        global the_number_of_requests
        the_number_of_requests = 0
    pre_time = cur_time
    
SmartCTL_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=one_more_syrup('SmartCTL'))
tactswitch_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=one_more_syrup('tactswitch'))
STOPswitch_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=STOP_motor)



#  メインループでステップモーターを回転させる
while True:
    if the_number_of_requests > 0:
        try:
            # モーターが回っていることを示すLED点灯
            led=15
            machine.Pin(led, machine.Pin.OUT).value(1)
            my_motor.step(angle)
            the_number_of_requests -= 1
            machine.Pin(led, machine.Pin.OUT).value(0)
        except Exception:
            pass
    elif the_number_of_requests == 0:
        pass
        
    
