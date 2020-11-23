import socket
import time
import sys
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080        # The port used by the server
# sys.exit(0)
def send_server(data):
    s.sendall(bytes(data, encoding='utf-8'))
    d = s.recv(1)
    len_data = ord(d)
    if(len_data == 0):
        len_word = ord(s.recv(1))
        len_incorrect = ord(s.recv(1))
        word_data = s.recv(len_word).decode('utf-8')
        incorrect_data = s.recv(len_incorrect).decode('utf-8')
        print(" ".join(word_data))
        print("Incorrect Guesses: " , " ".join(incorrect_data).upper())
    else:
        word_data = s.recv(len_data).decode('utf-8')
        print(word_data)
        s.close()
        sys.exit(0)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    letters_guessed = {}
    s.connect((HOST, PORT))
    letter = input("Ready to start the game? (y/n):")
    send_server(chr(0))
    while(True):
        letter = input("Letter to guess: ")
        if len(letter) > 0:
            print("Error! Please guess ONE letter. ")
            s.close()
            sys.exit(0)
        if not letter.isalpha():
            print("Error! Please guess one LETTER. ")
            s.close()
            sys.exit(0)
        letter = chr(ord(letter))
        letter_in_set = letter in letters_guessed
        if letter_in_set == False:
            print("Error! Letter " + letter + " has been guessed before, please guess another letter.")
            s.close()
            sys.exit(0)
        else:
            letters_guessed.add(letter)
        letters_guessed.add(letter)
        send_server(chr(1) + letter)
   
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

