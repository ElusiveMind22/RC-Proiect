import random
import uuid

'''
    Package class is a used to format packets
'''


class Package:
    # creates all the fields and fills them with data
    def __init__(self):
        self.OP = bytes([0x01])         # message code
        self.HTYPE = bytes([0x01])      # hardware address type
        self.HLEN = bytes([0x06])       # hardware address length
        self.HOPS = bytes([0x00])       # used by relay agents
        self.XID = bytes([random.randint(0, 0xFF) for _ in range(0, 4)])   # transaction id
        self.SECS = bytes([0x00, 0x00])   # seconds elapsed since client began address acquisition or renewal precess
        self.FLAGS = bytes([0x00, 0x00])
        self.CIADDR = bytes([0x00, 0x00, 0x00, 0x00])   # client's ip address
        self.YADDR = bytes([0x00, 0x00, 0x00, 0x00])    # 'your'(client) ip address offered by the server
        self.SIADDR = bytes([0x00, 0x00, 0x00, 0x00])   # server's ip address
        self.GIADDR = bytes([0x00, 0x00, 0x00, 0x00])   # relay agent ip address

        mac = uuid.getnode()        # mac address in decimal
        mac_bytes = []
        for _ in range(0, 6):
            mac_bytes.append(mac % 0x100)
            mac = int(mac / 0x100)
        mac_bytes = list(reversed(mac_bytes))
        for _ in range(0, 10):
            mac_bytes.append(0x00)
        self.CHADDR = bytes(mac_bytes)   # client's hardware address
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

    def __str__(self):
        result = ""
        result = result + f"OP: {int(self.OP)}\n"
        result = result + f"HTYPE: {int(self.HTYPE)}\n"
        result = result + f"HLEN: {int(self.HLEN)}\n"
        result = result + f"HOPS: {int(self.HOPS)}\n"

        result = result + f"XID: {self.XID}\n"

        result = result + f"SECS: {self.SECS}\n"
        result = result + f"FLAGS: {self.FLAGS}\n"

        result = result + "CIADDR: "
        for i in range(0, len(self.CIADDR)):
            result = result+f"{int(self.CIADDR)} "

        result = result + f"\nYADDR: "
        for i in range(0, len(self.YADDR)):
            result = result+f"{int(self.YADDR)} "

        result = result + f"\nSIADDR: "
        for i in range(0, len(self.SIADDR)):
            result = result+f"{int(self.SIADDR)} "

        result = result + f"\nGIADDR: "
        for i in range(0, len(self.GIADDR)):
            result = result+f"{int(self.GIADDR)}"

        result = result + f"\nCHADDR: "
        for i in range(0, len(self.CHADDR)):
            result = result+f"{int(self.CHADDR)} "

        # You need to translate the options from hexa to string
        result = result + "\nOPTIONS: "



    # when you receive a packet from the socket you set it as the new content
    # this means that you update the fields
    def setData(self, new_pack):
        self.OP = bytes([new_pack[0]])  # message code
        self.HTYPE = bytes([new_pack[1]])  # hardware address type
        self.HLEN = bytes([new_pack[2]])  # hardware address length
        self.HOPS = bytes([new_pack[3]])  # used by relay agents
        self.XID = bytes([new_pack[i] for i in range(4,8)])  # transaction id
        self.SECS = bytes([new_pack[8], new_pack[9]])  # seconds elapsed since client began address acquisition or renewal precess
        self.FLAGS = bytes([new_pack[10], new_pack[11]])
        self.CIADDR = bytes([new_pack[i] for i in range(12, 16)])  # client's ip address
        self.YADDR = bytes([new_pack[i] for i in range(16, 20)])  # 'your'(client) ip address offered by the server
        self.SIADDR = bytes([new_pack[i] for i in range(20, 14)])  # server's ip address
        self.GIADDR = bytes([new_pack[i] for i in range(24, 28)])  # relay agent ip address

        self.OPTIONS = bytes([new_pack[i] for i in range(236, len(new_pack))])  # dhcp options field( To be completed)

