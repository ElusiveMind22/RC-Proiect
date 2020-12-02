import re, uuid, sys
import random
from Package import Package
from PyQt5.QtWidgets import QApplication, QLabel
from struct import *

'''
print(':'.join(re.findall('..','%012x' %int(uuid.getnode()<<8))))
#print(len(uuid.getnode()))

print(sys.getsizeof(uuid.getnode()<<16))
h=[0x00000000]
print(24*h)
'''
# pack=Package()
# pack.printPack()

# print(f"{[random.randint(0, 0xFF) for _ in range(0,4)]}")
'''
mac=uuid.getnode()
mac_bytes = []
for _ in range(0,6):
    mac_bytes.append(mac % 0x100)
    mac=int(mac/0x100)
print(hex(uuid.getnode()))
mac_bytes=(list(reversed(mac_bytes)))
for _ in range(0,10):
    mac_bytes.append(0x00)
print(f"{bytes(mac_bytes)}")
print(f"{bytes([0xff,0x12,0x3])}")
print(f"{bytes([random.randint(0, 0xFF) for _ in range(0, 4)])}")
'''
# packet=bytes([0xff,0x12,0x3])
# print(len(packet))
'''
app = QApplication([])
label = QLabel("it works")
label.show()
app.exec_()
'''

var1=pack('BB', 1,2)
var1=[]
var1=var1+[1,2,3]
var1=var1+[4,5,6]
print("192.168.100.1".split("."))