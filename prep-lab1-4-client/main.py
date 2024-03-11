import socket, struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

string1 = str(input("string1 = "))
string2 = str(input("string2 = "))

s.connect(('192.168.1.143',1234))

send_string1 = string1.encode('utf-8')
len1 = len(send_string1)

send_string2 = string2.encode('utf-8')
len2 = len(send_string2)

s.send(struct.pack('!I', len1) + send_string1)
s.send(struct.pack('!I', len2) + send_string2)

res = s.recv(1024)
new_len = struct.unpack('!I',res[:4])[0]
new_res = res[4:4+new_len].decode('utf-8')

print("merged string = " + new_res)
s.close()