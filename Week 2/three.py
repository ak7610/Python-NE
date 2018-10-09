#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
from pprint import pprint
banner = ('#' * 160)
f = open('/Users/aman/Downloads/Python/Week 2/show_arp.txt')
read_file=f.readlines()
print(read_file)
print(len(read_file))
n = (read_file[1:])
pprint(n)
n.sort()
q = n[0:3]
print(banner)
print ('\n')
pprint(q)
print(banner)
print ('\n')
q = '\n'.join(q)
print(type(q))
print(q)
w = open('/Users/aman/Downloads/Python/Week 2/arp_entries.txt', mode='w')
w.write(q)
w.flush()
print('Doing it with python context manager method')
print(banner)
with open('/Users/aman/Downloads/Python/Week 2/arp_entries.txt', 'wt') as w:
    w.write(q)


