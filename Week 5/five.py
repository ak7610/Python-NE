from __future__ import print_function, unicode_literals
import re

with open('/Users/aman/Downloads/Python/Week 4/show_ipv6_intf.txt') as f:
    my_file = f.read()
match = re.search(r'IPv6 address:\s+(.*)\s+IPv6 subnet:', my_file, flags=re.DOTALL)
#print(match.group(1))
ipv6_addr = match.group(1).strip()
ipv6_list = ipv6_addr.splitlines()
#print(ipv6_list)
for index, value in enumerate(ipv6_list):
    #print (index)
    #print('#'*80)
    #print(value)
    address = re.sub(r'\[VALID\]', '', value)
    ipv6_list[index] = address.strip()
print()
print('-' * 80)
#print(ipv6_list)
print(ipv6_list[0])
print(ipv6_list[1])
print('-' * 80)
print()


