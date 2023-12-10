"""
Author: Eitan Shoshan
Program name: Ex-2.7 protocol
Description: the protocol used both in client and server data transporting
Date: 10-12-23
"""


def protocol_send(message):
    message_len = len(message)
    final_message = str(message_len) + '!' + message
    return final_message


def server_protocol_receive(my_socket):
    current_char = ''
    message_len = ''
    while current_char != '!':
        current_char = my_socket.recv(1).decode()
        message_len += current_char
    message_len = message_len[:-1]
    socket_output = my_socket.recv(int(message_len)).decode()
    if int(message_len) == len(socket_output):
        final_message = socket_output.split()
        return final_message
    else:
        return ["the data wasn't transported in full"]


def client_protocol_recieve(my_socket):
    current_char = ''
    message_len = ''
    while current_char != '!':
        current_char = my_socket.recv(1).decode()
        message_len += current_char
    message_len = message_len[:-1]
    socket_output = my_socket.recv(int(message_len)).decode()
    if int(message_len) == len(socket_output):
        return socket_output
    else:
        return "the data wasn't transported in full"
