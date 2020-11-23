#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
from game import *
import struct

def send_client(conn, game_state):
   send_msg = ""
   print("sent")
   status = game_state.status
   if(status == GameStatus.GAME_OUT_OF_GUESSES):
      msg = "You Lost!"
      flag = chr(len(msg))
      send_msg = bytes(flag+msg, encoding='utf-8')
      print("out",send_msg)
   elif(status == GameStatus.GAME_WON):
      msg = "You Won!"
      flag = chr(len(msg))
      print(flag+msg)
      send_msg = bytes(flag+msg, encoding='utf-8')
      print("won",send_msg)
   else:
      print('here2')
      word_state = ''.join(game_state.state)
      incorrect_guesses = ''.join(game_state.incorrect_guesses)
      word_len = chr(len(word_state))
      num_incorrect = chr(len(incorrect_guesses))
      send_msg = bytes(chr(0) + word_len + num_incorrect + word_state + incorrect_guesses, encoding='utf-8')
   print(send_msg)
   conn.sendall(send_msg)   

games = dict()
s = socket.socket()         # Create a socket object`
host = socket.gethostname() # Get local machine name
port = 8080                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

conn, addr = s.accept()     # Establish connection with client.
while True:

   # print('Got connection from', addr)
   d = conn.recv(1)
   if(d == b''):
      conn.close()
      break
   print(d)
   data_len = ord(d)
   print(data_len)
   if(data_len > 0):
      guess = conn.recv(data_len).decode('utf-8')
      print("GUESS",guess)
      state = games[addr].play_turn(guess)
      print(games[addr].state, state)
      send_client(conn, games[addr])
   else:
      print('here1')
      games[addr] = GameState("words.txt")
      send_client(conn, games[addr])

   print(addr)
   print(data_len)

   status = None

   
   # if(addr in games):
   #    game = games[addr]
   #    status = game.play_turn(data)
   #    str_state = ''.join(game.state)
   #    send_data = bytes(str(status) + str_state, encoding='utf-8')
   #    print('sent again')
   #    conn.sendall(send_data)
   # else:
   #    if(data == 'y'):
   #       print('y here')
   #       gs = GameState('words.txt',1)
   #       games[addr] = gs
   #       str_state = ''.join(gs.state)
   #       conn.sendall(bytes(str(GameStatus.GAME_START) + str_state, encoding='utf-8'))
   #    else:
   #       print("nah")
   #       conn.sendall(b'uhh nothing')

   # conn.send(b'Thank you for connecting')
   # c.close()                # Close the connection