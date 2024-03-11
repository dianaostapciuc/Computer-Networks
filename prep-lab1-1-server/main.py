import socket, struct
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # sock_stream is TCP
s.bind(('0.0.0.0', 1234)) # address and port
s.listen(3) # possible incoming clients
while True: # multiple clients??
    c, a = s.accept()
    s1 = c.recv(2)
    result1 = struct.unpack('!H', s1)[0]
    s2 = c.recv(2)
    result2 = struct.unpack('!H', s2)[0]
    suma = result2 + result1
    c.send(struct.pack('!H', suma))
    c.close()
