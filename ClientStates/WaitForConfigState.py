class WaitForConfigState:
    def __init__(self, client):
        self.client = client

    def start(self):
        while True:
            if self.client.config_ready:
                break
        self.client.current_state = 1
