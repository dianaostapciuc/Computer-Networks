import socket
import threading
import os


# here we use os for getting the contents of the file
def handle_client(client_socket):
    file_path = client_socket.recv(1024).decode('utf-8')
    try:
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            with open(file_path, 'rb') as file:
                file_content = file.read()
            response = f"File Size: {file_size}\nFile Content:\n{file_content.decode('utf-8')}"
        else:
            response = "File does not exist.\nFile Size: -1"

        client_socket.send(response.encode('utf-8'))

    except Exception as e:
        error_message = f"Error handling file: {str(e)}"
        client_socket.send(error_message.encode('utf-8'))
    client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 1234))
    server_socket.listen(5)

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()
