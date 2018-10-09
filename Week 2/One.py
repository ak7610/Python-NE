#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
f=open('/Users/aman/Downloads/Python/Week 2/Show_Version.txt')
show_ver=f.read()
print(show_ver)
print(type(show_ver))
f.close()
print('*' * 160)
print('\n')
print('Printing above output using Python Context Manager via readlines below: ')
print('\n')
print('*' * 160)
with open('/Users/aman/Downloads/Python/Week 2/Show_Version.txt') as f:
    show_ver=f.readlines()
    print(show_ver)
    print(type(show_ver))
    f.close()



