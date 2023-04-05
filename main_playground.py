#from stepper_arduino import Stepper
from stepper_qiita import Stepper
from time import sleep

number_of_steps = 2048
motor_pin_1 = 25
motor_pin_2 = 26
motor_pin_3 = 27
motor_pin_4 = 14
my_motor =  Stepper(number_of_steps, motor_pin_1, motor_pin_2, motor_pin_3, motor_pin_4)
my_motor.setSpeed(7)
rotation = 120
angle = rotation * number_of_steps

while True:
    try:
        led = 15
        machine.Pin(led, machine.Pin.OUT).value(1)
        time.sleep(1)
        machine.Pin(led, machine.Pin.OUT).value(0)
        my_motor.step(angle)
    except Exception:
        pass

