"""
    In this state the Client waits for the user to finish
    the packet configuration in the UI
    When the packet config is done the config_ready flag will be set on 1
    and the Client's state changes to the next state(SendConfigState)
"""


class WaitForConfigState:
    def __init__(self, client):
        self.client = client

    def start(self):
        while True:
            if self.client.config_ready:
                break
        self.client.config_ready = False
        self.client.current_state = 1
