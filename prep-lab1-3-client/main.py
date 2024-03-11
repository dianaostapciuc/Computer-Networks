import socket, struct
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.1.143', 1234))

string = str(input('string = '))
encode_string = string.encode('utf-8')
length = len(encode_string)

s.send(struct.pack('!I', length) + encode_string)
c = s.recv(1024)
new_str = c[4:4 + length].decode()
print("reversed string: " + new_str)
s.close()
