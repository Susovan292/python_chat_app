import time
import socket
import sys

SERVER_IP = input("Enter HOST ip : ")
SERVER_PORT = 2222
BUFFER_SIZE = 1024
SERVER_ADDRESS = (SERVER_IP, SERVER_PORT)


def start_client():
    UDP_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return UDP_client

def chat(UDP_CLIENT, BUFFER_SIZE, server_address):
    
    # send a message to the server.
    msg = input('>>> ')
    if msg == 'exit':
        sys.exit()

    msg_encoded = msg.encode('utf-8')
    UDP_CLIENT.sendto(msg_encoded, server_address)

    # recieve message from the server.
    response, server = UDP_CLIENT.recvfrom(BUFFER_SIZE)
    response_decoded = response.decode('utf-8')
    print(f"HOST[{server[0]}] <- {response_decoded}")


def main():
    UDP_CLIENT = start_client()
    while True:
        try:
            chat(UDP_CLIENT, BUFFER_SIZE, server_address=SERVER_ADDRESS)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
