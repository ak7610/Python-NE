#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
with open('/Users/aman/Downloads/Python/Week 2/show_ip_bgp_summ.txt') as f:
    var=f.readlines()
first = var[0].split()[7]
#print(first)
#autsys = first[5]
#asnum = first[7]
last = var[-1].split()[0]
#bgpPeer = last[0]
print(f'Local AS Number is: {first}')
print(f'BGP Peer IP Address is: {last}')

