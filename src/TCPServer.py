# TCP Server
#

from socket import *
from urllib import request
from multiprocessing import Process, Lock
import sys


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
    # message on server start
    print(f"[STARTING] TCP server startup initiated.")
    print(f"[STARTING] Configuring server settings...")

    # define default settings
    hostname = gethostname()
    network_addr = gethostbyname_ex(hostname)[2]
    public_addr = request.urlopen("https://api.ipify.org").read().decode()
    server_port = 8080

    # print server settings to console
    print(f"[SUCCESS] Settings are loaded.")
    print(f"[STARTING] hostname: { hostname }")
    print(f"[STARTING] network address: { network_addr }")
    print(f"[STARTING] public address: { public_addr }")

    # get port number from cmd args if given by user
    # if more arguments are given, they will be ignored
    print(f"[STARTING] Getting user supplied options...")
    if argc > 1:
        try:
            server_port = int(argv[1])
        except ValueError:
            print(f"[FAILURE] Incorrect port value given. Exiting...")
            sys.exit()

        print(f"[STARTING] Server will listen on port { server_port }.")

    else:
        print(f"[STARTING] No user supplied options detected.")
        print(f"[STARTING] Using fallback listening port { server_port }.")

    print(f"[SUCCESS] Server options are now configured.")

    # Setup socket for the server
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
