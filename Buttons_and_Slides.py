#!/usr/bin/python37all
import cgi
print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
print("selection = " + data.getvalue('option'))

slideData = cgi.FieldStorage()
if 'option' == 'led1':
  print("s1 = " + slideData.getvalue('slider1') + '<br>')
if 'option' == 'led2':
  print("s2 = " + slideData.getvalue('slider2') + '<br>')
if 'option' == 'led3':
  print("s3 = " + slideData.getvalue('slider3') + '<br>')
