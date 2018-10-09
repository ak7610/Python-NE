#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
i = (show_version.strip())
x = i.split()
model = x[1]
serial = x[2]
var1 = 'cisco' in model.lower()
var2 = '881' in model
check1 = print('Check if cisco is in model: {}'.format(var1))
check2 = print('Check if 881 is in model: {}'.format(var2))
print ("Serial Number: {}".format(serial))
print ("Serial Number: {}".format(model))