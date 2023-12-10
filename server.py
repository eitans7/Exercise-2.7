"""
Author: Eitan Shoshan
Program name: Ex-2.7 server
Description: the server of Exercise-2.7, doing functions according to the clients request.
Date: 10-12-23
"""
import socket
from protocol import *
from functions import *
import logging
import os


# MAX_PACKET = 4
IP = '0.0.0.0'
PORT = 1234
QUEUE_LEN = 1


LOG_FORMAT = '%(levelname)s | %(asctime)s | %(message)s'
LOG_LEVEL = logging.DEBUG
LOG_DIR = 'log'
LOG_FILE = LOG_DIR + '/server.log'


def call_func(parameter_list):
    if parameter_list[0] == "folder_dir":
        if len(parameter_list) == 2:
            return str(folder_dir(parameter_list[1]))
        else:
            return "parameters are wrong"

    elif parameter_list[0] == "delete":
        if len(parameter_list) == 2:
            return delete(parameter_list[1])
        else:
            return "parameters are wrong"

    elif parameter_list[0] == "copy":
        if len(parameter_list) == 3:
            return copy(parameter_list[1], parameter_list[2])
        else:
            return "parameters are wrong"

    elif parameter_list[0] == "execute":
        if len(parameter_list) == 2:
            return execute(parameter_list[1])
        else:
            return "parameters are wrong"

    elif parameter_list[0] == "screenshot":
        if len(parameter_list) == 1:
            return screenshot()
        else:
            return "no need of parameters"

    elif parameter_list[0] == "send_photo":
        if len(parameter_list) == 1:
            return send_photo()
        else:
            return "no need of parameters"

    elif parameter_list[0] == "the data wasn't transported in full":
        return "the data wasn't transported in full"

    else:
        return "undefined function"


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        my_socket.bind((IP, PORT))
        my_socket.listen(QUEUE_LEN)

        while True:
            client_socket, client_address = my_socket.accept()

            try:
                check = True
                while check:
                    msg = server_protocol_receive(client_socket)
                    logging.debug('the message received: ' + str(msg))

                    if msg != ["exit"]:
                        output = call_func(msg)
                        client_socket.send(protocol_send(output).encode())
                        logging.debug('the message sent: ' + output)
                    else:
                        check = False

            except socket.error as err:
                print('received socket error on client socket' + str(err))

            finally:
                print("client left")
                client_socket.close()

    except socket.error as err:
        print('received socket error on server socket' + str(err))

    finally:
        my_socket.close()


if __name__ == "__main__":
    if not os.path.isdir(LOG_DIR):
        os.makedirs(LOG_DIR)
    logging.basicConfig(format=LOG_FORMAT, filename=LOG_FILE, level=LOG_LEVEL)
    assert folder_dir("c:/temp") == ['c:/temp\\test2.txt', 'c:/temp\\test3.txt',
                                     'c:/temp\\test4.txt', 'c:/temp\\test5.txt']
    assert screenshot() != "an error was found"
    main()
