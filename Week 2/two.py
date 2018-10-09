#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
ip_list=['10.1.1.1', '20.1.1.1', '30.1.1.1', '40.1.1.1', '50.1.1.1']
ip_list.append('60.1.1.1')
ip_list.extend(['70.1.1.1', '80.1.1.1'])
print(ip_list)
new_list=['90.1.1.1', '100.1.1.1']
concat_list=ip_list + new_list
print (concat_list)
print(concat_list[0])
print(concat_list[-1])
concat_list.pop(0)
concat_list.pop(-1)
print(concat_list)
concat_list[0]='2.2.2.2'
print(concat_list[0])