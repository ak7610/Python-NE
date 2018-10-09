#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals
import os
WINDOWS = False
base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
# Ternary operator
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux
base_ip = '192.168.0.'
ip_list = []
for last_octet in range(1, 255):
    new_ip = base_ip + str(last_octet)
    ip_list.append(new_ip)
for index, ip_addr in enumerate(ip_list):
    print('{}--->{}'.format(index, ip_addr))
ip_list = ip_list[0:1]
print()
print('-' * 80)
for ip_addr in ip_list:
    print("IP Addr: ", ip_addr)
    return_code = os.system("ping -c 1 {}".format(ip_addr))
    print('-' * 80)
print('-' * 80)
print()
