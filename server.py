#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
from game import *

games = dict()
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8080                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

conn, addr = s.accept()     # Establish connection with client.

while True:
   print('Got connection from', addr)
   data = conn.recv(1024).decode('ascii')
   print(addr)
   print(data)
   status = None
   
   if(addr in games):
      game = games[addr]
      status = game.play_turn(data)
      str_state = ''.join(game.state)
      send_data = bytes(str(status) + str_state, encoding='utf-8')
      print('sent again')
      conn.sendall(send_data)
   else:
      if(data == 'y'):
         print('y here')
         gs = GameState('words.txt',1)
         games[addr] = gs
         str_state = ''.join(gs.state)
         conn.sendall(bytes(str(GameStatus.GAME_START) + str_state, encoding='utf-8'))
      else:
         print("nah")
         conn.sendall(b'uhh nothing')







   # conn.send(b'Thank you for connecting')
   # c.close()                # Close the connection