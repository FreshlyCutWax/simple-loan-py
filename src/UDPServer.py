# UDPServer
#

from socket import *

def main():
    server_port = 8080

    server_socket = socket(AF_INET, SOCK_DGRAM)

    server_socket.bind(('', server_port))

    while True:
        print("Waiting for UDP message...")

        message, client_addr = server_socket.recvfrom(2048)
        data = message.decode()
        
        print("Received data")

        data = data + " - Responded"

        print("Sending data")

        server_socket.sendto(data.encode(), client_addr)


if __name__ == "__main__":
    main()
