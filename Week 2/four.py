#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
from pprint import pprint
f = open('/Users/aman/Downloads/Python/Week 2/show_ip_int_brief.txt')
read = f.readlines()
entry = read[5]
s = entry.split()
intf = s[0]
ipaddr = s[1]
p = (intf, ipaddr)
print(type(p))
print(p)



