from __future__ import print_function, unicode_literals
import re
show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''
model_num = re.search(r'^Cisco (?P<Model_Number>\S+)', show_version, flags=re.M)
print(model_num.groupdict())
mem = re.search(r'^Cisco.* (?P<Memory>\d+K/\d+K)', show_version, flags=re.M)
print(mem.groupdict())


