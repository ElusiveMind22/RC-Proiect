import re,uuid,sys
from Package import Package
'''
print(':'.join(re.findall('..','%012x' %int(uuid.getnode()<<8))))
#print(len(uuid.getnode()))
print(hex(uuid.getnode()<<16))
print(sys.getsizeof(uuid.getnode()<<16))
h=[0x00000000]
print(24*h)
'''
#pack=Package()
#pack.printPack()
