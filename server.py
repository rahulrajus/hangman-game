#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
from game import *
import struct
import threading
import sys 

def send_client_msg(conn, msg):
   flag = chr(len(msg))
   print(flag+msg)
   send_msg = bytes(flag+msg, encoding='utf-8')
   conn.sendall(send_msg) 

def send_client(conn, game_state):
   send_msg = ""
   status = game_state.status
   if(status == GameStatus.GAME_OUT_OF_GUESSES):
      msg = "You Lose: " + game_state.word
      flag = chr(len(msg))
      send_msg = bytes(flag+msg, encoding='utf-8')
   elif(status == GameStatus.GAME_WON):
      msg = "You Won! "
      flag = chr(len(msg))
      send_msg = bytes(flag+msg, encoding='utf-8')
   elif(status == GameStatus.GAME_SERVER_OVERLOAD):
      msg = "Server Overload!"
      flag = chr(len(msg))
      send_msg = bytes(flag+msg, encoding='utf-8')
   else:
      word_state = ''.join(game_state.state)
      incorrect_guesses = ''.join(game_state.incorrect_guesses)
      word_len = chr(len(word_state))
      num_incorrect = chr(len(incorrect_guesses))
      send_msg = bytes(chr(0) + word_len + num_incorrect + word_state + incorrect_guesses, encoding='utf-8')
   conn.sendall(send_msg)   

games = dict()
s = socket.socket()         # Create a socket object`
host = socket.gethostname() # Get local machine name
port = 8080                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

def handleClient(conn, addr):
   while True:
         d = conn.recv(1)
         if(d == b''):
            conn.close()
            break
         data_len = ord(d)
         if(data_len > 0):
            guess = conn.recv(data_len).decode('utf-8')
            games[addr].play_turn(guess)
            send_client(conn, games[addr])
         else:
            word_idx = ord(conn.recv(1)) 
            if word_idx == 0:
               nextIdx = ord(conn.recv(1)) 
               if nextIdx == 0:
                  games[addr] = GameState("words.txt",rand=True)
               else:
                  games[addr] = GameState("words.txt", word_num=word_idx)
            else:
               nextIdx = ord(conn.recv(1)) 
               games[addr] = GameState("words.txt", word_num=word_idx)
            send_client(conn, games[addr])

while True:
   conn, addr = s.accept()  
   num_clients = threading.active_count()-1
   if(num_clients == 3):
      send_client_msg(conn, "Server Overload!")
   threading.Thread(target=handleClient, args=(conn, addr)).start()