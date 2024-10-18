# TCP Server
#

from socket import *
import sys
from multiprocessing import Process, Lock


def connection_manager():
    print("Start some connections")
    pass


def connection():
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


def main(argc, argv):
    # this is the default port number if none specified
    server_port = 8080
    server_socket = None

    # get port number from cmd args if given by user
    # if more arguments are given, they will be ignored
    if argc > 1:
        try:
            server_port = int(argv[1])
        except ValueError:
            print("Incorrect port value given.\nExiting...")
            sys.exit()

    # Server setup
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', server_port))

    # start listening for new connections
    server_socket.listen(1)

    # Process
    proc_connmgr = Process(target=connection_manager, args=())
    proc_connmgr.start()
    proc_connmgr.join()
    server_socket.close()
        

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
