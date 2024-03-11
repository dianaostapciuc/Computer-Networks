import socket
import struct

# create socket used for communication TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

string = str(input("string = "))

# connect to server (IP address and chosen port)

s.connect(("192.168.1.143", 1234))

# send the data

encode_string = string.encode('utf-8')
length = len(encode_string)
s.send(struct.pack('!I', length) + encode_string)

# receive the answer
result = s.recv(4)
result = struct.unpack('!I', result)

print("nr of spaces: " + str(result[0]))

# close

s.close()
