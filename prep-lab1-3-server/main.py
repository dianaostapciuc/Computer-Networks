import socket, struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0',1234))
s.listen(3)

while True:
    client, adr = s.accept()
    packed_str = client.recv(1024)
    length = struct.unpack('!I',packed_str[:4])[0]
    act_string = packed_str[4:4 + length].decode('utf-8')
    rev_string = ""
    for char in reversed(act_string):
        rev_string += char
    new_rev = rev_string.encode('utf-8')
    client.send(struct.pack('!I', length) + new_rev)
    client.close()