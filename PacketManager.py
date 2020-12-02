from Package import Package
from struct import *
'''
    This class has the purpose of converting a list of options
    into a package configuration and extracting the data from
    a package for display purposes
    The Packet Manager also triggers the client to start sending the packets
    
'''


class PacketManager:
    def __init__(self, uiManager, client):
        self.uiManager = uiManager
        self.client = client
        self.packet=Package()

    def setPackage(self, packet):
        self.packet=packet

    def convertToPackets(self, config):
        options_pack=[]
        for line in config:
            options = line.split()
            # this is the extension number, id decides the way you create the packet
            # the cases where you directly complete the parameters
            if int(options[0]) != 50 and int(options[0]) != 54:
                options_pack=options_pack+[int(options[0]), len(options)-1]
                options_pack=options_pack+[int(options[i]) for i in range(1, len(options))]
            else:   # optiunea contine un IP sau ceva ce nu poate fi convertit direct
                options_pack = options_pack+[int(options[0]), 4]    # functioneaza daca am un IP
                options_pack = options_pack+[int(num) for num in options[1].split(".")]

        return bytes(options_pack)

    def convertToDisplay(self, package):
        pass
