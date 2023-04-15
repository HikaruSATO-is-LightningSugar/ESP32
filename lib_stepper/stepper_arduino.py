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


