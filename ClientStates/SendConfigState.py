class SendConfigState:
    def __init__(self, client):
        self.client = client

    def start(self):
        # TO_DO
        # send the data to an address
        self.client.current_state = 2
