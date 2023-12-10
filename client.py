"""
Author: Eitan Shoshan
Program name: Ex-2.7 client
Description: the client of Ex-2.7, can ask the server to do multiple functions for him,
             including using parameters.
Date: 10-12-23
"""
import socket
from protocol import *
from functions import *
import os
import logging

# MAX_PACKET = 1024
IP = '127.0.0.1'
PORT = 1234


LOG_FORMAT = '%(levelname)s | %(asctime)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/client.log'


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.connect((IP, PORT))
        check = True
        while check:
            func = input("enter a function")
            func = func.lower()
            my_socket.send(protocol_send(func).encode())
            logging.debug('the func sent: ' + func)
            if func != "exit":
                response = client_protocol_recieve(my_socket)
                logging.debug('the message received: ' + response)
                print(response)
                if func == "send_photo":
                    process_server_response(response)
            else:
                check = False

    except socket.error as err:
        print('received socket error ' + str(err))

    finally:
        print("client left the server")
        my_socket.close()


if __name__ == "__main__":
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)
    main()
