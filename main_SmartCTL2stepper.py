# stepper_arduino.pyを使っていてのエラー
# 途中で止めて（＝ESP32を再起動させて）再度回転さた場合と
# テンションがかかりはじめるタイミングとで、
# 時計回りになったり、反時計回りになったり
# 回転方向が一定しない、、、、
# なんでだろう
# setSpeed() を10→6に変更して、トルクをあげてみる

#from stepper_arduino import Stepper
from stepper_qiita import Stepper
import time
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
my_motor.setSpeed(10)
# 回転数の指定
# 実験1（6rpm）：10500μL/510s/60回転　→　80μL/4s/0.5回転
# 実験2（6rpm）：
rotation = 0.5
# 回転数×360°
angle = rotation * number_of_steps


# スイッチが押された時、SmartCTLから信号が来た時
# 割り込みでモーター回転リクエストを１追加
# 参考
# https://tech-and-investment.com/raspberrypi-pico-12-gpio/
# http://tech-and-investment.com/raspberrypi-pico-14-gpio-interrupt/
# https://micropython-docs-ja.readthedocs.io/ja/latest/esp32/quickref.html
# https://goma483549.hatenablog.com/entry/2021/09/18/104726

the_number_of_requests = 0
SmartCTL_pin = machine.Pin(35, machine.Pin.IN, machine.Pin.PULL_UP)
tactswitch_pin = machine.Pin(34, machine.Pin.IN, machine.Pin.PULL_UP)
STOPswitch_pin = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)
# 割り込み処理の関数定義
# 簡単な処理になるように工夫
def callback(p):
    print('callback function is called!')
    the_number_of_requests = the_number_of_requests + 1
def STOP_motor():
    the_number_of_requests = 0
SmartCTL_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=callback)
tactswitch_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=callback)
STOPswitch_pin.irq(trigger=machine.Pin.IRQ_RISING, handler=STOP_motor)

#  メインループでステップモーターを回転させる
while the_number_of_requests > 0:
    try:
        # モーターが回っていることを示すLED点灯
        led=15
        machine.Pin(led, machine.Pin.OUT).value(1)
        time.sleep(1)
        machine.Pin(led, machine.Pin.OUT).value(0)
        my_motor.step(angle)
        the_number_of_requests -= 1
        time.sleep(1.0)
    except Exception:
        pass
    
