#!/usr/bin/python37all


import RPi.GPIO as GPIO
import cgi

# import and enable special exception handler for better error reporting
import cgitb
cgitb.enable()

ledPin1 = 19
ledPin2 = 13
ledPin3 = 26

# GPIO setup:
GPIO.setmode(GPIO.BCM)      # choose pin numbering convention (alt = BOARD)
GPIO.setwarnings(False)     # ignore warnings due to multiple scripts at same time
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(ledPin3, GPIO.OUT)



print("Content-type: text/html\n\n")
form = cgi.FieldStorage()
print("selection = " + form.getvalue('option'))

form = cgi.FieldStorage() # get POST data
if (form.getValue('option') == 'led1'): # changed from OFF to ON
  GPIO.output(ledPin1, 1)
  GPIO.output(ledPin3, 1)

if (form.getValue('option') == 'led2'):
  GPIO.output(ledPin1, 0)
  GPIO.output(ledPin3, 0)



##if 'option' == 'led1':
 ## print("s1 = " + slideData.getvalue('slider1') + '<br>')
##if 'option' == 'led2':
 ## print("s2 = " + slideData.getvalue('slider2') + '<br>')
##if 'option' == 'led3':
 ## print("s3 = " + slideData.getvalue('slider3') + '<br>')
