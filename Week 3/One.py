#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
from pprint import pprint
vlan_list = []
with open('/Users/aman/Downloads/Python/Week 3/show_vlan.txt') as f:
    var1 = f.read()
    var1 = var1.splitlines()
for line in var1:
    if 'VLAN' in line or '----' in line or line.startswith(' '):
        continue
    field = line.split()
    vlan_id = field[0]
    vlan_name = field[1]
    vlan_list.append((vlan_id, vlan_name))
pprint(vlan_list)




