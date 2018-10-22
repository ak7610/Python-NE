#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
import re
with open('/Users/aman/Downloads/Python/Week 4/Show_Version.txt') as f:
    output = f.read()
os_version = re.search(r"^Cisco.* Version (.*),", output, flags=re.M)
print('OS Version: {}'.format(os_version.group(1)))
serial_num = re.search(r'^\*0.*(F\S+)', output, flags=re.M)
print('Serial Number: {}'.format(serial_num.group(1)))
#conf_reg = re.search(r'^Configuration register.* (0\S+)', output, flags=re.M)
conf_reg = re.search(r'^Configuration register is (\S+)', output, flags=re.M)
print(f'Configuration Register: {conf_reg.group(1)}')
