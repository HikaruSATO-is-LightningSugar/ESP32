import time
import pigpio

LED_R_PIN = 13
LED_G_PIN = 19

pi = pigpio.pi()
pi.set_mode(LED_R_PIN, pigpio.OUTPUT)
pi.set_mode(LED_G_PIN, pigpio.OUTPUT)
while True:
    pi.write(LED_R_PIN, 1)
    pi.write(LED_G_PIN, 0)
    time.sleep(1)
    pi.write(LED_R_PIN, 0)
    pi.write(LED_G_PIN, 1)
    time.sleep(1)
