from ClientStates.WaitForConfigState import WaitForConfigState
from ClientStates.SendConfigState import SendConfigState
from ClientStates.WaitForReplyState import WaitForReplyState
from ClientStates.DisplayReplyState import DisplayReplyState
from Package import Package
from threading import Thread

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

    def setPackage(self, package):
        self.package = package

    def run(self):
        while True:
            print(f"Client's current state {self.current_state}")
            self.state[self.current_state].start()
