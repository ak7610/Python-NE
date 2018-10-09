#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals

ipv6_addr1 = "2001:db8:1234::1"
IPV6_ADDR1 = "2001:db8:1234::2"
ipV6_Addr3 = "2001:db8:1234::3"
print("")
print ("Is variable1 equals variable2: {}".format(ipv6_addr1 == IPV6_ADDR1))
print ("Is variable1 not equal to variable3: {}".format(ipv6_addr1 != ipV6_Addr3))
print("")
