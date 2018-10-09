#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
port_id, sys_name = (None, None)
with open("/Users/aman/Downloads/Python/Week 3/show_lldp_neighbors_detail.txt") as f:
    var1 = f.read()
    var1 = var1.splitlines()
for line in var1:
        field = line.split()
        if 'Port id' in line:
            port_id = field[2]
            print(f'Port ID: {port_id}')
        elif 'System Name' in line:
            sys_name = field[2]
            print(f'System Name: {sys_name}')
        if port_id and sys_name:
            break



