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
        self.packet = Package()

    def setPackage(self, packet):
        self.packet = packet

    def convertToPackets(self, config):  # unfinished
        options_pack = []
        terminator_needed = False
        for line in config:
            options = line.split()
            # this is the extension number, id decides the way you create the packet
            # the cases where you directly complete the parameters
            if int(options[0]) != 50 and int(options[0]) != 54:
                options_pack = options_pack + [int(options[0]), len(options) - 1]
                options_pack = options_pack + [int(options[i]) for i in range(1, len(options))]
                if int(options[0]) == 55 or int(options[1]) == 7:
                    terminator_needed = True
            else:  # optiunea contine un IP sau ceva ce nu poate fi convertit direct
                options_pack = options_pack + [int(options[0]), 4]  # functioneaza daca am un IP
                options_pack = options_pack + [int(num) for num in options[1].split(".")]
        if terminator_needed:
            options_pack.append(255)
        # after the package option field is successfully created
        # the information must be stored into a complete package
        # self.packet.OPTIONS = bytes(options_pack)#
        self.client.package.OPTIONS = bytes(options_pack)  #

        print("Packet Manager: ", options_pack)
        # after the config is done the package must be sent to
        # the client component
        # self.client.setPackage(self.packet)#

        # set the client as ready
        self.client.config_ready = True

        # return bytes(options_pack)

    # this method converts the bytes of the package into
    # human readable data
    def convertToDisplay(self, byte_string_package):
        packet_rcv = Package()
        packet_rcv.setData(byte_string_package)
        if packet_rcv.OPTIONS[2] == 2 or packet_rcv.OPTIONS[2] == 5:
            self.client.package.CIADDR = packet_rcv.YADDR
        self.uiManager.viewButton.setHidden(False)

        # save in the file the latest ip address
        numeric_ip = []
        if packet_rcv.OPTIONS[2] == 5:
            numeric_ip = [int(byte) for byte in packet_rcv.YADDR]
            with open("IP_History", 'w') as file:
                ip_addr = f"{numeric_ip[0]}.{numeric_ip[1]}.{numeric_ip[2]}.{numeric_ip[3]}"
                file.write(ip_addr)
        print(f"Packet manager:\n{packet_rcv}")
