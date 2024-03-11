import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind(('0.0.0.0', 7777))

    while True:
        message, addr = s.recvfrom(1024)
        decoded_message = message.decode('ascii')
        print(f"Received message from {addr}: {decoded_message}")
