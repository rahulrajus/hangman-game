from read_words import read_words
from enum import Enum

class GameStatus(Enum):
    GAME_SERVER_OVERLOAD = 0
    GAME_START = 1
    GAME_INCOMPLETE = 2
    GAME_WON = 3
    GAME_INCORRECT_GUESS = 4
    GAME_REPEAT_GUESS = 5
    GAME_INVALID_GUESS = 6
    GAME_LOST = 7
    GAME_OUT_OF_GUESSES = 8

class GameState:
    def __init__(self, words_file, word_num=0):
        words = read_words(words_file)
        self.word = words[word_num]
        self.state = ['_']*len(self.word)
        self.incorrect_guesses = list()
        self.previous_guesses = set()
        self.MAX_GUESSES = 6
        self.status = GameStatus.GAME_START
    
    def play_turn(self, letter):
        '''
        Input: letter:str
        Output: boolean, msg
        '''
        letter = letter.lower()
        
        if(not letter.isalpha()):
            self.status = GameStatus.GAME_INVALID_GUESS
            return GameStatus.GAME_INVALID_GUESS
        if(len(self.incorrect_guesses) == self.MAX_GUESSES):
            self.status = GameStatus.GAME_OUT_OF_GUESSES
            return GameStatus.GAME_OUT_OF_GUESSES

        if(letter in self.previous_guesses):
            self.status = GameStatus.GAME_REPEAT_GUESS
            return GameStatus.GAME_REPEAT_GUESS

        self.previous_guesses.add(letter)
        found = False
        for w in range(len(self.word)):
            if(self.word[w] == letter):
                self.state[w] = letter
                found = True
        if(not found):
            self.incorrect_guesses.append(letter)
            self.status = GameStatus.GAME_INCORRECT_GUESS
            return GameStatus.GAME_INCORRECT_GUESS
        if("".join(self.state) == self.word):
            self.status = GameStatus.GAME_WON
            return GameStatus.GAME_WON
        self.status = GameStatus.GAME_INCOMPLETE
        return GameStatus.GAME_INCOMPLETE

class Game:
    def __init__(self, words_file, word_num=0):
        if(words_file):
            self.words = read_words(words_file)
        else:
            raise FileNotFoundError("Please input a file")
        self.gs = GameState(self.words[word_num])
    def start_game(self, word_num):
        self.gs = GameState(self.words[word_num])
        return self.gs

    def play_turn(self, letter):
        return self.gs.play_turn(letter)

    def play(self):
        game = self.start_game(1)
        while(True):
            print(game.state)
            print("Incorrect Guesses: ", ' '.join(game.incorrect_guesses))
            letter = input("Guess?")
            res = game.play_turn(letter)
            if(res == GameStatus.GAME_INCORRECT_GUESS):
                print("Incorrect Guess!")
            elif(res == GameStatus.GAME_WON):
                print("You won!")
                break 
            elif(res == GameStatus.GAME_OUT_OF_GUESSES):
                print("You ran out of guesses :(")
                break       

    



    

        
