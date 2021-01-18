from Client import *
"""
    In this state the client sends the packet to the server
    and the Client's state changes to the next(WaitForReplyState)
"""


class SendConfigState:
    def __init__(self, client):
        self.client = client

    def start(self):
        # TO_DO
        # send the data to an address
        print(self.client.package.OPTIONS)
        bytes_to_send=self.client.package.getContent()
        self.client.socket_cl.sendto(bytes_to_send, self.client.DESTINATION)
        self.client.current_state = 2
