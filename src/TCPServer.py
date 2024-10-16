# TCP Server
#

from socket import *

def main():
    # initialize port and socket interface
    server_port = 8080
    server_socket = socket(AF_INET, SOCK_STREAM)

    # assign port to server's socket
    server_socket.bind(('', server_port))

    # start listening for new connections
    server_socket.listen(1)

    while True:
        # establish new connection w/ client socket
        print("Waiting for TCP connection...")
        connection_socket, addr = server_socket.accept()
        message = connection_socket.recv(1024)
        data = message.decode()

        # modified received data
        print("Connection established, modifying data")
        data = data + " - Responded"

        # send modified data
        print("Sending data")
        message = data.encode()
        connection_socket.send(message)
        connection_socket.close()

        print("Connection closed.")


if __name__ == "__main__":
    main()
