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
        print("Ended the connection with server at port 8080")
        sys.exit(0)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    letters_guessed = set()
    s.connect((HOST, PORT))
    letter = input("Ready to start the game? (y/n):")
    if(letter == 'n'):
        print("Ok! Goodbye!")
        quit()
    if(letter == 'y'):
        send_server(chr(0) + chr(0) + chr(0))
    else:
        send_server(chr(0) + chr(int(letter)) + chr(1))
    while(True):
        letter = input("Letter to guess: ")
        if len(letter) > 1:
            print("Error! Please guess ONE letter. ")
            continue
        if not letter.isalpha():
            print("Error! Please guess one LETTER. ")
            continue
        letter = chr(ord(letter))
        if letter in letters_guessed:
            print("Error! Letter " + letter + " has been guessed before, please guess another letter.")
            continue
        else:
            letters_guessed.add(letter)
        send_server(chr(1) + letter)