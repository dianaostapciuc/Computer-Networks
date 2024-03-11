import struct
import socket

# create the socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the server to the client(s)
s.bind(('0.0.0.0', 1234))

# listen for incoming connections
s.listen(3)

while True:
    client, addr = s.accept()

    # Receive the packed data containing the string length and string
    packed_data = client.recv(1024)

    # Unpack the data to get the string length
    length = struct.unpack('!I', packed_data[:4])[0]

    # Extract the string based on the length
    received_string = packed_data[4:4 + length].decode('utf-8')

    # Count spaces in the received string
    nr_spaces = received_string.count(" ")

    # Send the count of spaces back to the client
    client.send(struct.pack('!I', nr_spaces))

    client.close()
