#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
import pprint
import re
my_dict = {'ip_addr': '10.1.1.1', 'vendor': 'Juniper', 'username': 'ak7610', 'password': 'pass'}
#print(type(my_dict))
print(my_dict['ip_addr'])
if my_dict['vendor'] == 'Cisco':
    my_dict['Platform'] = 'ios'
elif my_dict['vendor'] == 'Juniper':
    my_dict['Platform'] = 'Junos'
#print(my_dict)
bgp_fields = {'bgp_as': '100', 'peer_as': '200', 'peer_ip': '1.1.1.1'}
my_dict.update(bgp_fields)
print(my_dict)
for key in my_dict:
    print('{:>15}'.format(key))
print('#' * 100)
for key, value in my_dict.items():
    print('{Key:>15} ----->{Value:>15}'.format(Key=key, Value=value))



