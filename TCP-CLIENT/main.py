import socket
import struct

# sending a number, a list, a list of numbers

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = str(input("What is the IP? "))

print(f'Connecting on server {IP}...')
s.connect((IP, 1234))

nr_to_send = int(input("send number> "))
string_to_send = str(input("string to send> "))
list_to_send = list(map(int, input("Enter a list of integers separated by space: ").split()))

# Pack the data (number, string length, string, and list of integers)
data_to_send = struct.pack("!I I", nr_to_send, len(string_to_send)) + string_to_send.encode('utf-8') + struct.pack(f"!{len(list_to_send)}I", *list_to_send)
print('Sending the data...')
s.send(data_to_send)

data = s.recv(1024)
message = data.decode('utf-8')
print(message)
s.close()
