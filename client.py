import socket
import time
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'y')
    data = s.recv(1024)
    print(data)
    time.sleep(1)
    print("next")
    s.sendall(b'u')
    data = s.recv(1024)
    print(data)
    time.sleep(1)
    print("next")
    s.sendall(b't')
    data = s.recv(1024)
    print(data)

    time.sleep(1)
    print("next")
    s.sendall(b'z')
    data = s.recv(1024)
    print(data)

