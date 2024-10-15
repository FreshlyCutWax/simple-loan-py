# UDPClient

from socket import *

def main():
    # assign server and destination port
    server_name = "localhost"
    server_port = 8080
    
    client_socket = socket(AF_INET, SOCK_DGRAM)

    data = "My Message"

    # message passing
    message = data.encode()
    client_socket.sendto(message, (server_name, server_port))
    response, server_addr = client_socket.recvfrom(2048)

    print(response.decode())


if __name__ == "__main__":
    main()
