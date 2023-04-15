from machine import Pin

LED_PIN = 18

led = Pin( LED_PIN, Pin.OUT )

led.value( 0 )