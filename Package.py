import random
import uuid

'''
    BIG PROBLEM AT THE CONVERSION 
    YOU NEED TO FIND A WAY TO CONVERT FROM INT TO BYTE ARRAYS
'''

class Package:
    def __init__(self):
        self.OP = bytes([0x01])         # message code
        self.HTYPE = bytes([0x01])      # hardware address type
        self.HLEN = bytes([0x06])       # hardware address length
        self.HOPS = bytes([0x00])       # used by relay agents
        self.XID = bytes.fromhex(f"{hex(random.randint(0, 0xFFFFFFFF))}")    # transaction id
        self.SECS = bytes([0x00, 0x00])         # seconds elapsed since client began address acquisition or renewal precess
        self.FLAGS = bytes([0x00, 0x00])
        self.CIADDR = bytes([0x00, 0x00, 0x00, 0x00])   # client's ip address
        self.YADDR = bytes([0x00, 0x00, 0x00, 0x00])    # 'your'(client) ip address offered by the server
        self.SIADDR = bytes([0x00, 0x00, 0x00, 0x00])   # server's ip address
        self.GIADDR = bytes([0x00, 0x00, 0x00, 0x00])   # relay agent ip address
        self.CHADDR = bytes(uuid.getnode() << 80)   # client's hardware address
        self.SNAME = bytes(64*[0x00,])     # optional server host name
        self.FILE = bytes(128*[0x00,])     # boot file name
        self.OPTIONS = bytes([0x00])        # dhcp options field( To be completed)

    def getContent(self):
        pack = self.OP + self.HTYPE + self.HLEN + self.HOPS + self.XID + self.SECS + self.FLAGS + self.CIADDR  \
            + self.YADDR + self.SIADDR + self.GIADDR + self.CHADDR + self.SNAME + self.FILE + self.OPTIONS

        return pack

    def printPack(self):
        print(f"OP: {self.OP}\nHTYPE: {self.HTYPE}\nHLEN: {self.HLEN}\nHOPS: {self.HOPS}\nXID{self.XID}\nSECS: {self.SECS}\nFLAGS: {self.FLAGS}\n"
              f"CIADDR: {self.CIADDR}\nYADDR: {self.YADDR}\nSIADDR: {self.SIADDR}\nGIADDR: {self.GIADDR}\nCHADDR: {self.CHADDR}\nSNAME: {self.SNAME}\n"
              f"FILE: {self.FILE}\nOPTIONS: {self.OPTIONS}")
