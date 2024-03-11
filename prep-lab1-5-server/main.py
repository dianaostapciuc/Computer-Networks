import socket, struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('0.0.0.0', 1234))
s.listen(3)

while True:
    client, addr = s.accept()
    data = client.recv(2)
    nr = struct.unpack('!H', data)[0]
    d = 1
    list_div = []
    while d <= nr:
        if nr % d == 0:
            list_div.append(d)
        d += 1
    result = ""
    for div in list_div:
        result += str(div)
        result += ' '

    client.send(result.encode('utf-8'))
    client.close()
