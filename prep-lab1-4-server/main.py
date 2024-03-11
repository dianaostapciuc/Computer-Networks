import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 1234))
s.listen(3)

while True:
    client, addr = s.accept()
    packed_data = client.recv(1024)

    # Unpack the length of the first string
    len1 = struct.unpack('!I', packed_data[:4])[0]

    # Extract the first string
    string1 = packed_data[4:4 + len1].decode('utf-8')

    current_index = len1 + 4  # 4 is the first length

    len2 = struct.unpack('!I', packed_data[current_index:current_index + 4])[0]
    string2 = packed_data[current_index + 4:current_index + 4 + len2].decode('utf-8')
    # Now, you have both strings

    merged_string = ""
    i = j = 0
    while i < len1 and j < len2:
        if string1[i] <= string2[j]:
            merged_string += string1[i]
            i += 1
        if string1[i] > string2[j]:
            merged_string += string2[j]
            j += 1
    merged_string += string1[i:]
    merged_string += string2[j:]

    coded_result = merged_string.encode('utf-8')
    res_len = len(coded_result)
    client.send(struct.pack('!I', res_len) + coded_result)
    client.close()