from shrp_gp2 import GP2
import RPi.GPIO as GPIO
import time

_IN1 = 17
_IN2 = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(_IN1, GPIO.OUT)
GPIO.setup(_IN2, GPIO.OUT)

in1 = GPIO.PWM(_IN1, 500)
in2 = GPIO.PWM(_IN2, 500)

gp = GP2()

try:
    f_fan = False
    error_count = 0
    in1.start(100)
    in2.start(0)
    while(True):
        dist = gp.distance
        if dist < 0:
            error_count += 1
            if error_count > 10:
                if f_fan:
                    in1.ChangeDutyCycle(0)
                    f_fan = False
                error_count = 0
            continue
        if dist < 63:
            duty = dist * 100 / 10
            if duty > 100:
                duty = 100
            print( duty)
            in1.ChangeDutyCycle(duty)
            if not f_fan:
                f_fan = True
        time.sleep(10)
    
except KeyboardInterrupt:
    in1.stop()
    in2.stop()

GPIO.cleanup()
