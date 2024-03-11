import socket
import threading
import subprocess


# here we used the subprocess to run the command

def handle_client(client_socket):
    # receive the command from the client
    command = client_socket.recv(1024).decode('utf-8')
    print(f"Received command: {command}")

    try:
        # execute the command and capture the output
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # send the output and exit code back to the client
        response = f"Exit Code: {result.returncode}\nOutput:\n{result.stdout}\nError:\n{result.stderr}"
        client_socket.send(response.encode('utf-8'))

    except Exception as e:
        error_message = f"Error executing command: {str(e)}"
        client_socket.send(error_message.encode('utf-8'))

    # close the client socket
    client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 1234))
    server_socket.listen(5)

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # Start a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()
