import socket
import sys
import select

# Import msvcrt for Windows
if sys.platform == 'win32':
    import msvcrt

def is_data_available():
    if sys.platform == 'win32':
        return msvcrt.kbhit()
    else:
        _, ready_to_read, _ = select.select([sys.stdin], [], [], 0)
        return sys.stdin in ready_to_read

def read_input():
    if sys.platform == 'win32':
        return msvcrt.getch().decode()
    else:
        return sys.stdin.readline()

def main():
    host = '192.168.1.143'
    port = 9034

    try:
        # Create a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        sock.connect((host, port))

        print(f"Connected to {host}:{port}")

        # Set the socket to non-blocking mode
        sock.setblocking(0)

        # Add the server socket to the list of inputs
        inputs = [sock]

        while True:
            if is_data_available():
                # Data from the keyboard
                message = read_input()
                sock.send(message.encode())

            readable, _, _ = select.select(inputs, [], [])

            for s in readable:
                # Data from the server
                data = s.recv(1024)
                if not data:
                    print("Server has closed the connection... closing.")
                    sys.exit(2)
                else:
                    sys.stdout.write(data.decode())
                    sys.stdout.flush()

    except socket.error as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
