from ClientStates.WaitForConfigState import WaitForConfigState
from ClientStates.SendConfigState import SendConfigState
from ClientStates.WaitForReplyState import WaitForReplyState
from ClientStates.DisplayReplyState import DisplayReplyState
from threading import Thread

class Client(Thread):
    def __init__(self):
        Thread.__init__(self)
        print("Client created")
        self.state = [WaitForConfigState(self), SendConfigState(self), WaitForReplyState(self), DisplayReplyState(self)]
        self.current_state = 0
        self.config_ready = False  # this flags the packet as being ready to send and is set from the UI callback
        self.reply_received = False  # this flags the receiving of a packet and is set from the WaitForReplyState

    def run(self):
        while True:
            print(f"Client's current state {self.current_state}")
            self.state[self.current_state].start()
