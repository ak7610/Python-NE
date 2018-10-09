#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
found1, found2 = (False, False)
with open("/Users/aman/Downloads/Python/Week 3/show_arp.txt") as f:
    var1 = f.read()
    var1 = var1.splitlines()
    for line in var1:
        if 'Protocol' in line:
            continue
        field = line.split()
        ip_addr = field[1]
        mac_addr = field[3]
        if '10.220.88.1' in line:
            print(f'Default gateway IP/MAC is: {ip_addr}/{mac_addr}')
            found1 = True
        elif '10.220.88.30' in line:
            print(f'Arista3 IP/Mac is: {ip_addr}/{mac_addr}')
            found2 = True
        if found1 and found2:
            print('Exiting...')
            break





