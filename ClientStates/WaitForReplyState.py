from Client import *
from Package import *
"""
    In this state the Client waits for the reply(from the server).
    If a certain amount of time passes and the server doesn't answer
    then the current state changes to the last state(SendConfigState),
    this cycle will be repeated a finite amount of times then the Client will stop
    If the server replies then the current state changes to the next(DisplayReplyState).
"""


class WaitForReplyState:
    def __init__(self, client):
        self.client = client

    def start(self):
        # TO_DO
        # wait for reply and save the packet
        print("Waiting for reply")
        try:
            server_reply, addr = self.client.socket_cl.recvfrom(self.client.MAX_BYTES)
            self.client.received_bytes=server_reply
        except:
            print("Waiting for a reply timed out\n")
        self.client.current_state = 3
