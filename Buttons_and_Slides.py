#!/usr/bin/python37all

#import necessary modules
import cgi
import json

import cgitb # import and enable special exception handler for better error reporting

cgitb.enable()

data = cgi.FieldStorage()

s1 = data.getvalue('slider1')
LED = data.getvalue('option')


print("Content-type: text/html\n\n")
print('<html>')
print('<form action="/cgi-bin/led.py" method="POST" target="_self">')
print('<input type="radio" name="option" value="led1"> Led 1 <br>')
print('<input type="radio" name="option" value="led2"> Led 2 <br>')
print('<input type="radio" name="option" value="led3"> Led 3 <br>')
print('<br>')
print('Adjust Brightness of Led <br>')
print('<input type="range" name="slider1" min ="0" max="100" value ="%s"/><br>' %s1)

LedData ={}
LedData = {'option':LED, 'slider':s1}

with open('Lab4_text.txt', 'w') as f:
  json.dump(LedData,f)

print('<input type="submit" value="submit">')

print('</form>')

print('</html>')


