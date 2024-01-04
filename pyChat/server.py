import time
import socket
import sys


class Server:
    
    SERVER_IP = socket.gethostbyname(socket.gethostname())
    clients = []
    def __init__(self, server_port=2222, buffer_size=1024):
        self.SERVER_PORT = server_port
        self.BUFFER_SIZE = buffer_size
        print(f"share this HOST ip to client : {Server.SERVER_IP}")

    def start_udp_server(self):
        UDP_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        UDP_server.bind((self.SERVER_IP, self.SERVER_PORT))
        print("Server is ready.")
        return UDP_server

    def start_chat(self, host):
        # receiving message from clients.
        print("waiting for client's message")
        encoded_msg, client = host.recvfrom(self.BUFFER_SIZE)

        if client not in Server.clients:
            Server.clients.append(client)
            print(f"New client {client[0]} added total clients= {len(Server.clients)}")

        decoded_msg = encoded_msg.decode('utf-8')
        print(f"CLIENT[{client[0]}] <- {decoded_msg}")


        # sending response to the client.
        response = input(">>> ")
        if response == 'exit':
            response.exit()
        response_encoded = response.encode('utf-8') 
        host.sendto(response_encoded, client)



def main():
    myServer = Server(server_port=2222, buffer_size=1024)
    while True:
        try:
            myServer.start_chat(host=myServer.start_udp_server())
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
