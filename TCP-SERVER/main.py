import socket
import struct
import threading


def handle_client(client_socket, address):
    data = client_socket.recv(1024)

    # Unpack the number and string length
    receive_nr, str_len = struct.unpack("!I I", data[:8])

    # Unpack the string
    receive_string = data[8:8 + str_len].decode('utf-8')

    # Unpack the list of integers
    list_offset = 8 + str_len
    list_length = (len(data) - list_offset) // 4  # Calculate the number of integers
    receive_list = struct.unpack(f"!{list_length}I", data[list_offset:list_offset + 4 * list_length])

    print(f'The IP is> {address}')
    print(f'The received number is {receive_nr}')
    print(f'The received string is {receive_string}')
    print(f'The received list is {receive_list}')

    print('Sending a message back...')

    message = 'The server received the data!'
    sent_message = message.encode('utf-8')
    client_socket.send(sent_message)
    client_socket.close()


def getting_data():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 1234))
    s.listen(5)
    print('Listening for connections on port 1234..')

    while True:
        client_socket, address = s.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()


if __name__ == "__main__":
    getting_data()
