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
        self.client.current_state = 3
