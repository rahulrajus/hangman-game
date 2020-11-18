from read_words import read_words

class GameState:
    def __init__(self, word):
        self.word = word 
        self.state = "_"*len(word)
        self.incorrect_guesses = list()
    
    def play_turn(self, letter):
        '''
        Input: letter:str
        Output: boolean, msg
        '''
        pass

class Game:
    def __init__(self, words_fiile):
        if(words_fiile):
            self.words = read_words(words_fiile)
        else:
            raise FileNotFoundError("Please input a file")



    

        
