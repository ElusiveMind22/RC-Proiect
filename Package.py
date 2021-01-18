import random
import uuid
from struct import *
'''
    Package class is a used to format packets
'''


class Package:
    # creates all the fields and fills them with data
    def __init__(self):
        self.OP = bytes([0x01])  # message code
        self.HTYPE = bytes([0x01])  # hardware address type
        self.HLEN = bytes([0x06])  # hardware address length
        self.HOPS = bytes([0x00])  # used by relay agents
        self.XID = bytes([random.randint(0, 0xFF) for _ in range(0, 4)])  # transaction id
        self.SECS = bytes([0x00, 0x00])  # seconds elapsed since client began address acquisition or renewal precess
        self.FLAGS = bytes([0x80, 0x00])
        self.CIADDR = bytes([0x00, 0x00, 0x00, 0x00])  # client's ip address
        self.YADDR = bytes([0x00, 0x00, 0x00, 0x00])  # 'your'(client) ip address offered by the server
        self.SIADDR = bytes([0x00, 0x00, 0x00, 0x00])  # server's ip address
        self.GIADDR = bytes([0x00, 0x00, 0x00, 0x00])  # relay agent ip address

        mac = uuid.getnode()  # mac address in decimal
        mac_bytes = []
        for _ in range(0, 6):
            mac_bytes.append(mac % 0x100)
            mac = int(mac / 0x100)
        mac_bytes = list(reversed(mac_bytes))
        for _ in range(0, 10):
            mac_bytes.append(0x00)
        self.CHADDR = bytes(mac_bytes)  # client's hardware address
        self.SNAME = bytes(64 * [0x00, ])  # optional server host name
        self.FILE = bytes(128 * [0x00, ])  # boot file name
        self.MAGIC_COOKIE = bytes([0x63, 0x82, 0x53, 0x63])
        self.OPTIONS = bytes([0x00])  # dhcp options field( To be completed)

    def getContent(self):
        # the string of bytes is a multiple of 64
        pack = self.OP + self.HTYPE + self.HLEN + self.HOPS + self.XID + self.SECS + self.FLAGS + self.CIADDR \
               + self.YADDR + self.SIADDR + self.GIADDR + self.CHADDR + self.SNAME + self.FILE + self.MAGIC_COOKIE + self.OPTIONS

        return pack

    def printPack(self):
        print(
            f"OP: {self.OP}\nHTYPE: {self.HTYPE}\nHLEN: {self.HLEN}\nHOPS: {self.HOPS}\nXID{self.XID}\nSECS: {self.SECS}\nFLAGS: {self.FLAGS}\n"
            f"CIADDR: {self.CIADDR}\nYADDR: {self.YADDR}\nSIADDR: {self.SIADDR}\nGIADDR: {self.GIADDR}\nCHADDR: {self.CHADDR}\nSNAME: {self.SNAME}\n"
            f"FILE: {self.FILE}\nMAGIC COOKIE: {self.MAGIC_COOKIE}\nOPTIONS: {self.OPTIONS}")

    # this method is used when the client displays the message from the server
    def __str__(self):
        result = ""
        result = result + f"OP: {(self.OP)}\n"
        result = result + f"HTYPE: {(self.HTYPE)}\n"
        result = result + f"HLEN: {(self.HLEN)}\n"
        result = result + f"HOPS: {(self.HOPS)}\n"

        result = result + f"XID: {self.XID}\n"

        result = result + f"SECS: {self.SECS}\n"
        result = result + f"FLAGS: {self.FLAGS}\n"

        result = result + "CIADDR: "
        for i in range(0, len(self.CIADDR)):
            result = result + f"{(self.CIADDR[i])} "

        result = result + f"\nYADDR: "
        for i in range(0, len(self.YADDR)):
            result = result + f"{(self.YADDR[i])} "

        result = result + f"\nSIADDR: "
        for i in range(0, len(self.SIADDR)):
            result = result + f"{(self.SIADDR[i])} "

        result = result + f"\nGIADDR: "
        for i in range(0, len(self.GIADDR)):
            result = result + f"{(self.GIADDR[i])}"

        result = result + f"\nCHADDR: "
        for i in range(0, len(self.CHADDR)):
            result = result + f"{(self.CHADDR[i])} "

        # You need to translate the options from hexa to string
        result = result + "\nOPTIONS:\n"

        # the server reply has the following pattern:
        # CODE[1] LEN[1] DATA[LEN]
        # The following piece of code is supposed to iterate trough the bytes in the option field
        # and translate them into human readable information
        # things i can decode:
        # subnet mask; router; IP lease time; DHCP server; DNS; domain name; time offset;
        # time server;
        index=0
        while index < len(self.OPTIONS):
            # i always starts on the CODE position
            if self.OPTIONS[index] == 53:
                result = result + "DHCP message type: "
                type = self.OPTIONS[index + 2]
                if type == 2:
                    result = result + "Offer\n"
                elif type == 5:
                    result = result + "Acknowledge\n"
                elif type == 6:
                    result = result + "Not Acknowledge\n"
                else:
                    result = result + f"{type}\n"
                index += 3
            elif self.OPTIONS[index]== 1:
                result= result+f"Subnet Mask: {self.OPTIONS[index+2]}.{self.OPTIONS[index+3]}" \
                               f".{self.OPTIONS[index+4]}.{self.OPTIONS[index+5]}\n"
                index += 6
            elif self.OPTIONS[index]==3:
                result = result + f"Router: {self.OPTIONS[index + 2]}.{self.OPTIONS[index + 3]}" \
                                  f".{self.OPTIONS[index + 4]}.{self.OPTIONS[index + 5]}\n"
                index += 6
            elif self.OPTIONS[index]==51:
                value=self.OPTIONS[index+2]*(256^3)+self.OPTIONS[index+3]*(256^2)\
                      +self.OPTIONS[index+4]*256 +self.OPTIONS[index+5]
                result=result+f"IP address lease time: {value}\n"
                index+=6
            elif self.OPTIONS[index]== 54:
                result = result + f"DHCP server: {self.OPTIONS[index + 2]}.{self.OPTIONS[index + 3]}" \
                                  f".{self.OPTIONS[index + 4]}.{self.OPTIONS[index + 5]}\n"
                index += 6
            elif self.OPTIONS[index]==6:
                result=result+"Domain Name Server:"
                index+=1
                length=self.OPTIONS[index]
                index+=1
                for _ in range(0, int(length/4)):
                    result=result+f"{self.OPTIONS[index]}.{self.OPTIONS[index + 1]}" \
                                  f".{self.OPTIONS[index + 2]}.{self.OPTIONS[index + 3]}\n"
                    index+=4
                index+=1
            elif self.OPTIONS[index]==15:
                result=result+"Domain Name: "
                index+=1
                length=self.OPTIONS[index]
                for _ in range(0,length):
                    index+=1
                    result=result+f"{self.OPTIONS[index]}"
                result=result+"\n"
                index+=1
            elif self.OPTIONS[index]==2:
                index+=2
                result=result+f"Time Offset: {unpack('i',bytes(reversed(self.OPTIONS[index:index+4])))}\n"
                index+=4
            elif self.OPTIONS[index]==4:
                result=result+"Time Server:\n"
                index += 1
                length = self.OPTIONS[index]
                index += 1
                for _ in range(0, int(length / 4)):
                    result = result + f"{self.OPTIONS[index]}.{self.OPTIONS[index + 1]}" \
                                      f".{self.OPTIONS[index + 2]}.{self.OPTIONS[index + 3]}\n"
                    index += 4
                index+=1
            elif self.OPTIONS[index]==0 or self.OPTIONS[index]==255:
                break
            else:
                print(f"Unknown  Option {self.OPTIONS[index]}\n")
        return result

    # when you receive a packet from the socket you set it as the new content
    # this means that you update the fields
    def setData(self, new_pack):
        #check if this is correct
        self.OP = bytes([new_pack[0]])  # message code
        self.HTYPE = bytes([new_pack[1]])  # hardware address type
        self.HLEN = bytes([new_pack[2]])  # hardware address length
        self.HOPS = bytes([new_pack[3]])  # used by relay agents
        self.XID = bytes([new_pack[i] for i in range(4, 8)])  # transaction id
        self.SECS = bytes(
            [new_pack[8], new_pack[9]])  # seconds elapsed since client began address acquisition or renewal precess
        self.FLAGS = bytes([new_pack[10], new_pack[11]])
        self.CIADDR = bytes([new_pack[i] for i in range(12, 16)])  # client's ip address
        self.YADDR = bytes([new_pack[i] for i in range(16, 20)])  # 'your'(client) ip address offered by the server
        self.SIADDR = bytes([new_pack[i] for i in range(20, 24)])  # server's ip address
        self.GIADDR = bytes([new_pack[i] for i in range(24, 28)])  # relay agent ip address

        self.OPTIONS = bytes([new_pack[i] for i in range(240, len(new_pack))])  # dhcp options field( To be completed)
