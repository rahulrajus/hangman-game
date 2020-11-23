import socket
import time
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

def send_server(data):
    s.sendall(bytes(data, encoding='utf-8'))
    d = s.recv(1)
    print(d)
    len_data = ord(d)
    if(len_data == 0):
        len_word = ord(s.recv(1))
        len_incorrect = ord(s.recv(1))
        word_data = s.recv(len_word).decode('utf-8')
        incorrect_data = s.recv(len_incorrect).decode('utf-8')
        print(word_data)
        print(incorrect_data)
        print(len_data)
        print(len_word)
        print(len_incorrect)
    else:
        word_data = s.recv(len_data).decode('utf-8')
        print(word_data)
        s.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    send_server(chr(0))
    time.sleep(1)
    send_server(chr(1) + 'j')
    time.sleep(1)
    send_server(chr(1) + 't')
    time.sleep(1)
    send_server(chr(1) + 'z')
    time.sleep(1)
    send_server(chr(1) + 'a')
    time.sleep(1)
    s.close()

    # print("next")
    # s.sendall(b'1j')
    # data = s.recv(9).decode('utf-8')
    # print(data)
    # time.sleep(1)
    # print("next")
    # s.sendall(b'1t')
    # data = s.recv(9).decode('utf-8')
    # print(data)

    # time.sleep(1)
    # print("next")
    # s.sendall(b'1z')
    # data = s.recv(9).decode('utf-8')
    # print(data)

