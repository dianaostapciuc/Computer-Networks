import socket
import select


# Function to broadcast message to all clients
def broadcast_message(server_socket, message, client_sockets):
    for client_socket in client_sockets:
        # Send the message to all clients except the server and the sender
        if client_socket != server_socket:
            try:
                client_socket.send(message)
            except:
                # Remove the broken connection
                client_sockets.remove(client_socket)


# Function to handle new connections
def handle_new_connection(server_socket, client_sockets):
    client_socket, client_address = server_socket.accept()
    client_sockets.append(client_socket)

    print(f"New connection from {client_address}")

    # Send a welcome message to the new client
    welcome_message = f"Welcome! You are now connected. There are {len(client_sockets) - 1} clients online."
    client_socket.send(welcome_message.encode())

    # Broadcast the new connection to all clients
    broadcast_message(server_socket, f"Client {len(client_sockets)} has joined the chat.\n".encode(), client_sockets)


# Function to handle incoming messages
def handle_messages(client_socket, client_sockets):
    try:
        message = client_socket.recv(1024)
        if message:
            # Broadcast the message to all clients
            broadcast_message(server_socket, message, client_sockets)
        else:
            # Remove the broken connection
            client_sockets.remove(client_socket)
            print("Client disconnected")
            broadcast_message(server_socket, f"Client {len(client_sockets)} has left the chat.\n".encode(),
                              client_sockets)
    except:
        # Remove the broken connection
        client_sockets.remove(client_socket)
        print("Client disconnected")
        broadcast_message(server_socket, f"Client {len(client_sockets)} has left the chat.\n".encode(), client_sockets)


# Main function
# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('192.168.1.143', 9034))
server_socket.listen(10)
# List to keep track of client sockets
client_sockets = [server_socket]

print("Server is listening on port 9034...")

while True:
    # Use select to efficiently wait for input on multiple sockets
    readable, _, _ = select.select(client_sockets, [], [])

    for s in readable:
        if s == server_socket:
            # New connection
            handle_new_connection(server_socket, client_sockets)
        else:
            # Incoming message from a client
            handle_messages(s, client_sockets)
