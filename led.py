# micro python code
 
import machine
import utime
import random

red = machine.Pin(12, machine.Pin.OUT)
#red    = machine.Pin(21, machine.Pin.OUT)
green  = machine.Pin(14, machine.Pin.OUT)
yellow = machine.Pin(27, machine.Pin.OUT)
colors = [red, green, yellow]
#colors = [red, red, red]


for i in range(1000):
#    led = random.choice(colors)
    led = colors[i%3]
    
    a = random.uniform(0,   0.15)
    b = random.uniform(0.15, 0.3)
    sleep_time = a + b
    
    led.value(1)
    utime.sleep(0.15)
 #    utime.sleep(sleep_time * random.random())
    
    led.value(0)
    utime.sleep(0.15)
#    utime.sleep(sleep_time * random.random())
