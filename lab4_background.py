#!/usr/bin/python3

#importing modules
import RPi.GPIO as GPIO
import time
import json



#Led Pin Numbers
ledPin1 = 19
ledPin2 = 13
ledPin3 = 26

# GPIO setup:
GPIO.setmode(GPIO.BCM)      # choose pin numbering convention (alt = BOARD)
GPIO.setwarnings(False)     # ignore warnings due to multiple scripts at same time
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)

#Initial PWM Values
pwm_led1 = GPIO.PWM(ledPin1, 100)
pwm_led1.start(0)

pwm_led2 = GPIO.PWM(ledPin2, 100)
pwm_led2.start(0)

pwm_led3 = GPIO.PWM(ledPin3, 100)
pwm_led3.start(0)


while True:
  with open('Lab4_text.txt', 'r') as f:
    data=json.load(f)
    myLed = str(data['option'])
    slide = int(data['slider1'])
  
  if(myLed == 'led1'):
    dutyCycle1 = slide
    pwm_led1.ChangeDutyCycle(dutyCycle1)
  if(myLed == 'led2'):
    dutyCycle2 = slide
    pwm_led2.ChangeDutyCycle(dutyCycle2)
  if(myLed == 'led3'):
    dutyCycle3 = slide
    pwm_led3.ChangeDutyCycle(dutyCycle3)

  time.sleep(0.1)
