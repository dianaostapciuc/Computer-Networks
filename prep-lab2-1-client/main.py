import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.1.9', 1234))

command = str(input("command> "))
sent_command = command.encode('utf-8')

s.send(sent_command)

response = s.recv(1024).decode('utf-8')
print(response)

s.close()
