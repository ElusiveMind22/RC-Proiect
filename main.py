from Client import Client
import time



def main():
    client = Client()
    client.start()
    time.sleep(4)
    client.config_ready = True


main()
