# TCPClient
#

from socket import *

def main():
    # assign server and destination port
    server_name = "localhost"
    server_port = 8080

    client_socket = socket(AF_INET, SOCK_STREAM)

    data = "My Message"

    # message passing via connection
    message = data.encode()
    client_socket.connect((server_name, server_port))
    client_socket.send(message)
    response = client_socket.recv(1024)

    print(response.decode())


if __name__ == "__main__":
    main()
