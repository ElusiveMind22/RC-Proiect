"""
    In this state the Client sent to the UI manager the data that
    needs to be displayed to the user, after the state changes to
    the first state(WaitForConfigState)
"""


class DisplayReplyState:
    def __init__(self, client):
        self.client = client

    def start(self):
        # TO_DO
        # data will be extracted from the packet and then sent to the UI for display
        print("Displaying the reply")
        self.client.packet_manager.convertToDisplay(self.client.received_bytes)
        self.client.current_state = 0
