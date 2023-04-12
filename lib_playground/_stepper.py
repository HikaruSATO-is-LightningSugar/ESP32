# Stepper Motor setting
stepper_rpm = 7
motor_pin_1 = 32
motor_pin_2 = 33
motor_pin_3 = 25
motor_pin_4 = 26
# LED setting
moter_io_led_pin = 15


#from stepper_arduino import Stepper
from stepper_qiita import Stepper
import time
import utime
import machine

number_of_steps = 2048
my_motor =  Stepper(number_of_steps, motor_pin_1, motor_pin_2, motor_pin_3, motor_pin_4)
my_motor.setSpeed(stepper_rpm)
# 回転数の指定
# 実験1（絹糸、6rpm）：10500μL/510s/60回転　=　80μL/4s/0.5回転
# 実験2（テグス、7rpm）：
rotation = 0.5
angle = rotation * number_of_steps
moter_io_led = machine.Pin(moter_io_led_pin, machine.Pin.OUT)
the_number_of_requests = 10


#  メインループでステップモーターを回転させる
while True:
    if the_number_of_requests > 0:
        try:
            moter_io_led.value(1)
            my_motor.step(angle)
            the_number_of_requests -= 1
            moter_io_led.value(0)
        except Exception:
            pass
    elif the_number_of_requests == 0:
        pass
        
    

