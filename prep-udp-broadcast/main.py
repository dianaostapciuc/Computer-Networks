import socket
from time import sleep

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(b'Hi', ('255.255.255.255', 7777))
    print("Sent data..")
    s.close()
    sleep(1)
