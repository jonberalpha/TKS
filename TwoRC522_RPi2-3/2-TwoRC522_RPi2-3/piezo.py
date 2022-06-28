#!/usr/bin/env python
import RPi.GPIO as GPIO
import time


#def do_sound():
#    GPIO.setup(24,GPIO.OUT)    # Code For Turn ON/OFF Buzzer
#    GPIO.output(24,GPIO.HIGH)   # Code For Turn ON/OFF Buzzer
#    time.sleep(0.1)
#    GPIO.output(24,GPIO.LOW)
def do_sound():
    tonePin = 24
    GPIO.setmode(GPIO.BCM)
    #GPIO.setup(tonePin, GPIO.IN)
    GPIO.setup(tonePin, GPIO.OUT)
    p = GPIO.PWM(tonePin, 2500)
    #p.ChangeFrequency(250)
    p.start(50)     # parameter: duty-cycle
    time.sleep(1)
    p.stop()
    GPIO.cleanup()
