# ESP32 - MicroPythonを使い、ステッピングモータを制御する
# https://qiita.com/kotaproj/items/cd37c971f03fb02c97ce

import time
from machine import Pin

class Stepper():
    def __init__(self,  number_of_steps,
                 motor_pin_1, motor_pin_2, motor_pin_3, motor_pin_4):
        self.step_number = 0                   # which step the motor is on
        self.direction = 0                     # motor direction
        self.last_step_time = 0                # time stamp in us of the last step taken
        self.number_of_steps = number_of_steps  # total number of steps for this motor

        # setup the pins on the microcontroller:
        self.motor_pin_1 = Pin(motor_pin_1, Pin.OUT)
        self.motor_pin_2 = Pin(motor_pin_2, Pin.OUT)
        self.motor_pin_3 = Pin(motor_pin_3, Pin.OUT)
        self.motor_pin_4 = Pin(motor_pin_4, Pin.OUT)

        # pin_count is used by the stepMotor() method:
        self.pin_count = 4

        self.setSpeed()
        return

    def setSpeed(self, what_speed=10):
        ''' Sets the speed in revs per minute
        '''
        self.step_delay = 60 * 1000 * 1000 // self.number_of_steps // what_speed
        return

    def step(self, steps_to_move, auto_stop=True):
        ''' Moves the motor steps_to_move steps.  If the number is negative,
            the motor moves in the reverse direction.
        '''
        steps_left = abs(steps_to_move)  # how many steps to take

        # determine direction based on whether steps_to_mode is + or -:
        self.direction = 1 if steps_to_move > 0 else 0

        # decrement the number of steps, moving one step each time:
        while steps_left > 0:
            now = time.ticks_us()
            # move only if the appropriate delay has passed:
            if time.ticks_diff(now, self.last_step_time) >= self.step_delay:
                # get the timeStamp of when you stepped:
                self.last_step_time = now
                # increment or decrement the step number,
                # depending on direction:
                if self.direction == 1:
                    self.step_number += 1
                    if self.step_number == self.number_of_steps:
                        self.step_number = 0
                else:
                    if self.step_number == 0:
                        self.step_number = self.number_of_steps
                    self.step_number -= 1

                # decrement the steps left:
                steps_left -= 1
                # step the motor to step number 0, 1, 2, 3
                self.stepMotor(self.step_number % 4)

        if auto_stop:
            self.stop()
        return

    def stepMotor(self, this_step):
        ''' Moves the motor forward or backwards.
              if (this->pin_count == 4) {
        '''
        # 1010
        if this_step == 0:
            self.motor_pin_1.value(True)
            self.motor_pin_2.value(False)
            self.motor_pin_3.value(True)
            self.motor_pin_4.value(False)
        # 0110
        elif this_step == 1:
            self.motor_pin_1.value(False)
            self.motor_pin_2.value(True)
            self.motor_pin_3.value(True)
            self.motor_pin_4.value(False)
        # 0101
        elif this_step == 2:
            self.motor_pin_1.value(False)
            self.motor_pin_2.value(True)
            self.motor_pin_3.value(False)
            self.motor_pin_4.value(True)
        # 1001
        elif this_step == 3:
            self.motor_pin_1.value(True)
            self.motor_pin_2.value(False)
            self.motor_pin_3.value(False)
            self.motor_pin_4.value(True)
        return

    def stop(self):
        self.motor_pin_1.value(False)
        self.motor_pin_2.value(False)
        self.motor_pin_3.value(False)
        self.motor_pin_4.value(False)
        return
    


# MicroPython Stepper Motor Driver
# Code to drive a 28BYJ-48 motor attached to a ULN2003 driver.
# https://github.com/larsks/micropython-stepper-motor
class Motor:
    stepms = 10

    # Do be defined by subclasses
    maxpos = 0
    states = []

    def __init__(self, p1, p2, p3, p4, stepms=None):
        self.pins = [p1, p2, p3, p4]

        if stepms is not None:
            self.stepms = stepms

        self._state = 0
        self._pos = 0

    def __repr__(self):
        return '<{} @ {}>'.format(
            self.__class__.__name__,
            self.pos,
        )

    @property
    def pos(self):
        return self._pos

    @classmethod
    def frompins(cls, *pins, **kwargs):
        return cls(*[machine.Pin(pin, machine.Pin.OUT) for pin in pins],
                   **kwargs)

    def zero(self):
        self._pos = 0

    def _step(self, dir):
        state = self.states[self._state]

        for i, val in enumerate(state):
            self.pins[i].value(val)

        self._state = (self._state + dir) % len(self.states)
        self._pos = (self._pos + dir) % self.maxpos

    def step(self, steps):
        dir = 1 if steps >= 0 else -1
        steps = abs(steps)

        for _ in range(steps):
            t_start = time.ticks_ms()

            self._step(dir)

            t_end = time.ticks_ms()
            t_delta = time.ticks_diff(t_end, t_start)
            time.sleep_ms(self.stepms - t_delta)

    def step_until(self, target, dir=None):
        if target < 0 or target > self.maxpos:
            raise ValueError(target)

        if dir is None:
            dir = 1 if target > self._pos else -1
            if abs(target - self._pos) > self.maxpos/2:
                dir = -dir

        while True:
            if self._pos == target:
                break
            self.step(dir)

    def step_until_angle(self, angle, dir=None):
        if angle < 0 or angle > 360:
            raise ValueError(angle)

        target = int(angle / 360 * self.maxpos)
        self.step_until(target, dir=dir)


class FullStepMotor(Motor):
    stepms = 5
    maxpos = 2048
    states = [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 1],
    ]


class HalfStepMotor(Motor):
    stepms = 3
    maxpos = 4096
    states = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1],
    ]



# stepper.py

# A micropython driver for 4-phase, unipolar stepper motors such as
# the 28BYJ-48

# Relesed to the Public Domain by Nicko van Someren, 2020

# The constructor for the Stepper class takes as arguments the four
# pins for driving the motor phases, in phase order, and optionally a
# timer. The pins can be passed as pin numbers or machine.Pin objects
# and the timer can be a machine.Timer object or a timer index. Note
# that if two stepper motors use the same timer then they will not be
# able to run at the same time.
#
# The run() method takes a number of steps and an optional delay (in
# seconds) between driving the steps (the default is 1ms). A negative
# step count will drive the motor in the oposite direction to a
# positive count. The count represents "half steps" since the driver
# alternates driving single coils and driving pairs of adjacent coils.
# Calls to run() return immediately; the motor runs on a timer in the
# background. Calling run() again before the previous command has
# finished adds the new count to the old count, so the destination
# position is the sum of the requests; the delay is set to the new
# value if stepper is not already at its final location.
#
# The stop() method will stop the rotation of the motor. It returns
# the number of un-taken steps that would be needed to perform the
# outstanding requests from previous calls to run().
#
# The is_running property returns true if the motor is running,
# i.e. stop() would return a non-zero value, and false otherwise.

import machine
import time

# When the following number is sampled at four consecutive
# even-numbered bits it will have two bits set, but sampling at four
# consecutive odd-numbered bits will only yield one bit set.

_WAVE_MAGIC = 0b0000011100000111

class Stepper_gist:
    def __init__(self, A, B, C, D, T=1):
        if not isinstance(T, machine.Timer):
            T = machine.Timer(T)
        self._timer = T
        l = []
        for p in (A, B, C, D):
            if not isinstance(p, machine.Pin):
                p = machine.Pin(p, machine.Pin.OUT)
            l.append(p)
        self._pins = l
        self._phase = 0
        self._stop()
        self._run_remaining = 0

    def _stop(self):
        [p.off() for p in self._pins]

    # Note: This is called on an interrupt on some platforms, so it must not use the heap
    def _callback(self, t):
        if self._run_remaining != 0:
            direction = 1 if self._run_remaining > 0 else -1
            self._phase = (self._phase + direction) % 8
            wave = _WAVE_MAGIC >> self._phase
            for i in range(4):
                self._pins[i].value((wave >> (i*2)) & 1)
            self._run_remaining -= direction
        else:
            self._timer.deinit()
            self._stop()

    def run(self, count, delay=0.001):
        tick_hz=1000000
        period = int(delay*tick_hz)
        if period < 500:
            period = 500
        self._run_remaining += count
        if self._run_remaining != 0:
            self._timer.init(period=period, tick_hz=tick_hz,
                             mode=machine.Timer.PERIODIC, callback=self._callback)
        else:
            self._timer.deinit()
            self._stop()

    def stop(self):
        remaining = self._run_remaining
        self._run_remaining = 0
        self._timer.deinit()
        self._stop()
        return remaining

    @property
    def is_running(self):
        return self._run_remaining != 0# stepper.py




   

# Code example from YoungWorks blog on how to use a stepper motor
# https://www.youngwonks.com/blog/How-to-use-a-stepper-motor-with-the-Raspberry-Pi-Pico
from machine import Pin
import utime

pins = [
    Pin(13, Pin.Out),
    Pin(12, Pin.Out),
    Pin(14, Pin.Out),
    Pin(27, Pin.Out),
]

# one hot encoding vectors
full_step_sequence = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

while True:
    for step in full_step_sequence:
        for i in rang(len(pins)):
            pins[i].value(step[i])
            utime.sleep(0.001)
            
            
            
 #https://github.com/LanghiDev/MicroPython-with-Stepper-motor-28byj-48/blob/master/Stepper.py
# Stepper.py - Stepper library for MicroPython (ESP32) - Version 1.1.0
#
# Credits from Arduino Library
# Original library        (0.1)   by Tom Igoe.
# Two-wire modifications  (0.2)   by Sebastian Gassner
# Combination version     (0.3)   by Tom Igoe and David Mellis
# Bug fix for four-wire   (0.4)   by Tom Igoe, bug fix from Noah Shibley
# High-speed stepping mod         by Eugene Kozlenko
# Timer rollover fix              by Eugene Kozlenko
# Five phase five wire    (1.1.0) by Ryan Orendorff
# 
# Credits from MicroPython Library (made specifically for ESP32)
# Original library	 (0.1)	 by Nicolas C. Langhi
# Time modifications	 (0.2)	 by Davi Jose Garcia Viegas
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
#
# Drives a bipolar phase stepper motor.
#
# When wiring multiple stepper motors to a microcontroller, you quickly run
# out of output pins, with each motor requiring 4 connections.
#
#
# The sequence of control signals for 4 control wires is as follows:
#
# Step C0 C1 C2 C3
#    1  1  0  1  0
#    2  0  1  1  0
#    3  0  1  0  1
#    4  1  0  0  1
#
#
# The circuits for Arduino can be found at
#
# http://www.arduino.cc/en/Tutorial/Stepper


from machine import Pin
import time

class Stepper:
    def __init__(self, number_of_steps, pin1, pin2, pin3, pin4):
        # Inicializa o motor de passo.
        self.step_number = 0 # which step the motor is on
        self.direction = 0 # motor direction
        self.last_step_time = 0 # time stamp in us of the last step taken
        self.number_of_steps = number_of_steps
        
        self.step_delay = 0
        
        # Inicia a contagem a partir que o programa foi ligado
        self.micros = time.ticks_us()
        
        # Conexão e configuração da pinagem para o motor
        self.motor_pin_1 = Pin(pin1, Pin.OUT)
        self.motor_pin_2 = Pin(pin2, Pin.OUT)
        self.motor_pin_3 = Pin(pin3, Pin.OUT)
        self.motor_pin_4 = Pin(pin4, Pin.OUT)
        
        # pin_count é usado pelo método stepMotor()
        self.pin_count = 4;
    
    
    # Sets the speed in revs per minute
    def setSpeed(self, whatSpeed):
        self.step_delay = 60 * 1000 * 1000 / self.number_of_steps / whatSpeed
        
        
    # Moves the motor steps_to_move steps.  If the number is
    # negative, the motor moves in the reverse direction.
    def step(self, steps_to_move):
        steps_left = abs(steps_to_move) # Quantos passos irá dar
        
        # Determina direção com base no steps_to_move, se é + ou -
        if steps_to_move > 0:
            self.direction = 1
        if steps_to_move < 0:
            self.direction = 0
            
        # decrement the number of steps, moving one step each time:
        while steps_left > 0:
            now = time.ticks_us()-self.micros # Get microseconds time
            # move only if the appropriate delay has passed:
            if now - self.last_step_time >= self.step_delay:
                # get the timeStamp of when you stepped:
                self.last_step_time = now
                # Incrementa ou diminui o número de passo,
                # dependendo da direção:
                if self.direction == 1:
                    self.step_number += 1
                    if self.step_number == self.number_of_steps:
                        self.step_number = 0
                else:
                    if self.step_number == 0:
                        self.step_number = self.number_of_steps
                    self.step_number -= 1
                # Diminui o steps left:
                steps_left -= 1
                # step the motor to step number 0, 1, ..., {3 or 10}
                self.stepMotor(self.step_number % 4)
                
    
    def stepMotor(self, thisStep):
        if thisStep == 0: # 1010
            self.motor_pin_1.value(1)
            self.motor_pin_2.value(0)
            self.motor_pin_3.value(1)
            self.motor_pin_4.value(0)
        if thisStep == 1: # 0110
            self.motor_pin_1.value(0)
            self.motor_pin_2.value(1)
            self.motor_pin_3.value(1)
            self.motor_pin_4.value(0)
        if thisStep == 2: # 0101
            self.motor_pin_1.value(0)
            self.motor_pin_2.value(1)
            self.motor_pin_3.value(0)
            self.motor_pin_4.value(1)
        if thisStep == 3: # 1001
            self.motor_pin_1.value(1)
            self.motor_pin_2.value(0)
            self.motor_pin_3.value(0)
            self.motor_pin_4.value(1)
               
    # version() returns the version of the library:
    def version(self):
        return 5
    
    def micros():
        timer = time.ticks_us()
        return time.ticks_us()-timer



