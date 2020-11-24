Vamsi Desu and Rahul Rajan 
CS3251 - Hangman Game

To implement this game, we started with creating a game state, which keeps track of the overall state of the game as the game is being played. Within the GameStatus class, 
we also used an enum to determine the current status of the turn. Afterwards, we implemented a Game class, which contains the funcationality of playing the game till a win or loss. After the game structure was set, we decided to work on the client-server connection to establish actual gameplay. The client (client.py) consisted of creating a connection with the server and then sending the letter (while checking edge cases) to server. The server (server.py) then took that data and determined whether that letter was a correct guess and sent back a response. The work was divided into two parts - gameplay and client-server connection. Vamsi worked on the gameplay and Rahul worked on the server-client connection (in addition to implementing the proposed gameplay structure). We then worked together to put all the parts together. 

Word Dictionary (in words.txt):

jazz
buzz
hajj
fizz
jinx
huff
buff
jiff
junk
quiz
bass
make
sake
fake
rake

Test example logs are located in server.txt and client.txt




