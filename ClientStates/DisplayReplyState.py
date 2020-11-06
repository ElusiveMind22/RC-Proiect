class DisplayReplyState:
    def __init__(self, client):
        self.client = client

    def start(self):
        # TO_DO
        # data will be extracted from the packet and then sent to the UI for display
        self.client.current_state = 0
