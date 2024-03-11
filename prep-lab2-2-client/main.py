import socket
def run_client(file_path):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.9', 1234))

    client_socket.send(file_path.encode('utf-8'))

    response = client_socket.recv(4096).decode('utf-8')
    print(response)

    client_socket.close()


if __name__ == "__main__":
    user_file_path = input("Enter the file path: ")
    run_client(user_file_path)
