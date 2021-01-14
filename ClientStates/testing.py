# send a preconfigured dhcp discover and display the offer
from Package import *
import socket
SERVER_PORT=67
CLIENT_PORT=68
CLIENT_IP='0.0.0.0'
MAX_BYTES=1024
DESTINATION=('<broadcast>',SERVER_PORT)
SOURCE=(CLIENT_IP,5050)

inputs=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

#inputs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
inputs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
inputs.bind(('', CLIENT_PORT))
inputs.settimeout(5)

client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.settimeout(5)
client.bind(SOURCE)

packet=Package()
packet.OPTIONS=bytes([53,1,1, 50,4,192,168,1,100, 55,4,1,3,15,6,255])

print("Packet will be sent!")
bytes_to_send=packet.getContent()
client.sendto(bytes_to_send,DESTINATION)
print("Waiting for a response")
server_reply=inputs.recvfrom(MAX_BYTES)
print("Reply Received")
print(server_reply)


