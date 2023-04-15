import sys
import time
import pigpio

LED_PIN = 12
LED_PWM_FREQUENCY = 8000
LED_PWM_RANGE = 100
pwm_duty = float(sys.argv[1])

pi = pigpio.pi()
pi.set_mode(LED_PIN, pigpio.OUTPUT)
pi.set_PWM_frequency(LED_PIN, LED_PWM_FREQUENCY)
pi.set_PWM_range(LED_PIN, LED_PWM_RANGE)
pi.set_PWM_dutycycle(LED_PIN, int(pwm_duty * LED_PWM_RANGE))
