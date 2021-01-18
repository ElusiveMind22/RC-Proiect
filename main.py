from Client import Client
from UIManager import UIManager
from PacketManager import PacketManager
import time



def main():
    '''
    client = Client()
    client.start()
    time.sleep(4)
    client.config_ready = True
'''

    client = Client()
    ui=UIManager()
    pack_man = PacketManager(ui, client)
    ui.setPacketManager(pack_man)
    client.setPacketManager(pack_man)
    client.start()
    ui.startUI()
    print("Initialization ended")

main()
