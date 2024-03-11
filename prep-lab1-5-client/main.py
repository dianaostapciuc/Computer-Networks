import socket, struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.1.143',1234))

nr = int(input("number = "))

s.send(struct.pack('!H', nr))
c = s.recv(1024)
res = c.decode('utf-8')
print("divisors: " + res)