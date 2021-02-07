
"""
Program to detect the vibration sensor input (digial) and play any random buzzer tune.
Can be helpful to teach how random function can be used.
Author - Atul N Yadav
"""

from machine import Pin,PWM
import time
import random

# Construct PWM object, with LED on Pin(0).
pwm = PWM(Pin(0))

#Sensor on Pin 22 to detect vibration / touch
vibration_sensor= Pin(22, Pin.IN, Pin.PULL_DOWN)

while True:
    if vibration_sensor.value():
        print("Click - ")
        # Set the PWM frequency.
        intfreq = random.randint(100,1000) # Change this range between 0-1000
        pwm.freq(intfreq)
        print("frequency : ")
        # Set the Duty.
        print(intfreq)
        intduty = random.randint(1000,10000) # Change this range between 0-65025
        print("Duty : ")
        print(intduty)
        pwm.duty_u16(intduty)
        time.sleep(0.5)  # Change time
        
    else: #This logic stops the buzzer
        pwm.freq(500)
        pwm.duty_u16(0)
