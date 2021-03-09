# send a preconfigured dhcp discover and display the offer
from Package import *
import socket
SERVER_PORT=67
CLIENT_PORT=68
CLIENT_IP='0.0.0.0' # pe windows trebuie adresa pe care o am deja, detalii int laborator
MAX_BYTES=1024
DESTINATION=('<broadcast>',SERVER_PORT)
SOURCE=(CLIENT_IP,5050)

inputs=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

#inputs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
inputs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
inputs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


inputs.bind(('192.168.1.101', CLIENT_PORT))
inputs.settimeout(5)

#client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
#client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#client.settimeout(5)
#client.bind(SOURCE)

packet=Package()

# try to read the last ip used
numeric_ip=[]
try:
    with open("IP_History", 'r') as file:
        ip_addr=file.readline()
        numeric_ip = [int(number) for number in ip_addr.split('.')]
except:
    print("there's a problem with the file")

print(numeric_ip)


# sending a dhcp discover
if len(numeric_ip)==4:
    packet.OPTIONS = bytes([53, 1, 1, 50, 4, numeric_ip[0], numeric_ip[1], numeric_ip[2], numeric_ip[3]
                               , 55, 5, 1, 3, 15, 6, 4, 255])
else:
    packet.OPTIONS=bytes([53,1,1, 50,4,192,168,100,17, 55,5,1,3,15,6,4,255])
#packet.OPTIONS=bytes([53,1,1])
packet.printPack()
print("Packet will be sent!")
bytes_to_send=packet.getContent()
inputs.sendto(bytes_to_send,DESTINATION)
print("Waiting for a response")
server_reply, addr =inputs.recvfrom(MAX_BYTES)
packet.setData(server_reply)
print("Reply Received")
print(str(packet))
# update the ip history every dhcp ack(5)
if packet.OPTIONS[2]==5:
    numeric_ip=[int(byte) for byte in packet.YADDR]
with open("IP_History", 'w') as file:
    ip_addr=f"{numeric_ip[0]}.{numeric_ip[1]}.{numeric_ip[2]}.{numeric_ip[3]}"
    file.write(ip_addr)


# sending a dhcp request

packet.OP=bytes([0x01])
packet.CIADDR = packet.YADDR
packet.YADDR=bytes([0x00,0x00,0x00,0x00])
# I can get an ACK message when i use the address that the server assigned me
# I can force a NAK message when i use a bad address like 192.168.100.1
packet.OPTIONS=bytes([53,1,3, 50,4,packet.CIADDR[0],packet.CIADDR[1],packet.CIADDR[2],packet.CIADDR[3]
                         , 54,4,192,168,100,1])
bytes_to_send=packet.getContent()
inputs.sendto(bytes_to_send,DESTINATION)
print("Waiting for a response")
server_reply, addr =inputs.recvfrom(MAX_BYTES)
packet.setData(server_reply)
print("Reply Received")
print(str(packet))


#sending a dhcp release

packet.OP=bytes([0x01])
packet.YADDR=bytes([0x00,0x00,0x00,0x00])
packet.OPTIONS=bytes([53,1,7,255])
bytes_to_send=packet.getContent()
inputs.sendto(bytes_to_send,DESTINATION)
# there will be no reply from the server


#dhcp inform
'''
packet.OP=bytes([0x01])
packet.YADDR=bytes([0x00,0x00,0x00,0x00])
packet.OPTIONS=bytes([53,1,8])
bytes_to_send=packet.getContent()
inputs.sendto(bytes_to_send,DESTINATION)
# there will be no reply from the server
server_reply, addr =inputs.recvfrom(MAX_BYTES)
packet.setData(server_reply)
print("Reply Received")
print(str(packet))
'''
