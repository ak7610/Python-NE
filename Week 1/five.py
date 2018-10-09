#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
from __future__ import print_function, unicode_literals

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"
mac1 = mac1.split()
mac2 = mac2.split()
mac3 = mac3.split()
ip_addr1 = mac1[1]
ip_addr2 = mac2[1]
ip_addr3 = mac3[1]
mac_addr1 = mac1[3]
mac_addr2 = mac2[3]
mac_addr3 = mac3[3]
print ("{:>20}{:>20}".format("IP ADDR", "MAC ADDRESS"))
print (("-" * 20), " ", ("-" * 60))
print ("{:>20}{:>20}".format(ip_addr1, mac_addr1))
print ("{:>20}{:>20}".format(ip_addr2, mac_addr2))
print ("{:>20}{:>20}".format(ip_addr3, mac_addr3))

