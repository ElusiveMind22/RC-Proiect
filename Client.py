from ClientStates.WaitForConfigState import WaitForConfigState
from ClientStates.SendConfigState import SendConfigState
from ClientStates.WaitForReplyState import WaitForReplyState
from ClientStates.DisplayReplyState import DisplayReplyState
from Package import Package
from threading import Thread
import socket

"""
    Client is a class that has the following goals:
        -Receive a packets from a PacketManager and send the packets to the server
        -Receive packets from the server and forward them for display
    
    
    The Client implements the State design pattern and runs on a separate thread.
    Note:
        The client runs in a infinite state loop and it can stop for 2 reasons:
            1)The server doesn't respond
            2)The UI has been closed by the user (Don't let this thread run is the UI is closed).
"""


class Client(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Client created")
        self.state = [WaitForConfigState(self), SendConfigState(self), WaitForReplyState(self), DisplayReplyState(self)]
        self.current_state = 0
        self.config_ready = False  # this flags the packet as being ready to send and is set from the UI callback
        self.reply_received = False  # this flags the receiving of a packet and is set from the WaitForReplyState
        self.package = Package()
        self.received_bytes=bytes([0x00]) # this is the variable that holds the server reply
        self.keep_running=True

        # Creating the socket
        self.CLIENT_PORT = 68
        self.SERVER_PORT = 67
        self.MAX_BYTES = 1024
        self.DESTINATION = ('<broadcast>', self.SERVER_PORT)
        self.socket_cl=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.socket_cl.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.socket_cl.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket_cl.bind(('192.168.1.101', self.CLIENT_PORT))
        self.socket_cl.settimeout(5)
    def setPacketManager(self, packet_manager):
        self.packet_manager=packet_manager

    def setPackage(self, package):
        self.package = package

    def run(self):
        while self.keep_running:
            print(f"Client's current state {self.current_state}")
            self.state[self.current_state].start()
