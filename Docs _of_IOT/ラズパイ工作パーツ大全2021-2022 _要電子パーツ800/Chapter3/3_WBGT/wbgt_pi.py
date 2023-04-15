#!/usr/bin/env python3
#encoding=utf-8
## wbgt_pi
## スクリプト名：wbgt_pi.py
## 機能概要　　：AM2320から温度・湿度を測定しWBGTを計算
##　　　　　　 ：室内での熱中症警報をLEDで通知
##　　　　　　 ：15秒毎に再評価
##
## Presented by RaspiMAG 2020/10
## Programmed by pochi_ken
# ライブラリー定義
import RPi.GPIO as GPIO
import smbus
import math
import time

i2c = smbus.SMBus(1)
address = 0x5c

def wbgt_calc():
    time.sleep(0.003)
    i2c.write_i2c_block_data(address,0x03,[0x00,0x04])
    time.sleep(0.015)
    block = i2c.read_i2c_block_data(address,0,6)
    humi = float(block[2] << 8 | block[3])/10
    temp = float(block[4] << 8 | block[5])/10
    wbgt = math.ceil(float(0.725 * temp + 0.0368 * humi + 0.00364 * temp * humi - 3.246))
    print('temp:' + str(temp))
    print('humi:' + str(humi))
    print('wbgt:' + str(wbgt))
    return wbgt

def alert(wbgt):
    if wbgt >= 31:
        sel = 2
        wbgt_result = "Danger"
    elif wbgt < 31 and wbgt >= 28:
        sel = 10
        wbgt_result = "Strict caution"
    elif wbgt < 28 and wbgt >= 25:
        sel = 4
        wbgt_result = "Warning"
    elif wbgt < 25 and wbgt >= 21:
        sel = 3
        wbgt_result = "Caution"
    else:
        sel = 0
        wbgt_result = "Safe"
    print('WBGT Alert:' + str(wbgt_result))
    return sel

# setting up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
LED_pwm = [0, 0, 0]
duty = [0, 100, 34]
LED_list = [11, 13, 15]             # Blue, Green, Red
Color_list = [[1, 0, 0, 1, 0, 0],   # 0-Blue
              [0, 1, 0, 0, 1, 0],   # 1-Green
              [0, 0, 1, 0, 0, 1],   # 2-Red
              [1, 1, 0, 1, 1, 0],   # 3-Cian
              [0, 1, 1, 0, 1, 1],   # 4-Yellow
              [1, 0, 1, 1, 0, 1],   # 5-Magenta
              [1, 1, 1, 1, 1, 1],   # 6-White
              [1, 1, 0, 2, 1, 0],   # 7-Mint
              [1, 1, 0, 1, 2, 0],   # 8-light blue
              [0, 1, 1, 0, 1, 2],   # 9-Yellow green
              [0, 1, 1, 0, 2, 1],   #10-Orange
              [1, 0, 1, 1, 0, 2],   #11-Violet
              [1, 0, 1, 2, 0, 1],   #12-Pink
              [1, 1, 1, 2, 1, 1],   #13-Dark white
              [1, 1, 1, 1, 2, 1],   #14-Sakura
              [1, 1, 1, 1, 1, 2],   #15-Water blue
              [1, 1, 1, 2, 2, 1],   #16-Light pink
              [1, 1, 1, 1, 2, 2],   #17-Light violet
              [1, 1, 1, 2, 1, 2],   #18-Light green
              [0, 0, 0]]            #19-Black
GPIO.setup(LED_list, GPIO.OUT)
GPIO.output(LED_list, Color_list[19])

# Main
while True:
    try:
        i2c.write_i2c_block_data(address,0x00,[])
    except:
        pass

    wbgt = wbgt_calc()
    sel = alert(wbgt)

    for ch in range(3):
        LED_pwm[ch] = GPIO.PWM(LED_list[ch], 100)
        if Color_list[sel][ch] == 1:
            LED_pwm[ch].start(0)
    for ch in range(3):
         LED_pwm[ch].ChangeDutyCycle(duty[Color_list[sel][ch + 3]])
    time.sleep(15)

    for ch in range(3):
        LED_pwm[ch].stop()
GPIO.cleanup()

