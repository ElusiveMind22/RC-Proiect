class WaitForReplyState:
    def __init__(self, client):
        self.client = client

    def start(self):
        # TO_DO
        # wait for reply and save the packet
        self.client.current_state = 3
