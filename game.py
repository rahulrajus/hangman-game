from read_words import read_words

class GameState:
    def __init__(self, word):
        self.word = word 
        self.state = ['_']*len(word)
        self.incorrect_guesses = list()
        self.previous_guesses = set()
        self.MAX_GUESSES = 6
    
    def play_turn(self, letter):
        '''
        Input: letter:str
        Output: boolean, msg
        '''
        if(len(self.incorrect_guesses) == self.MAX_GUESSES):
            raise Exception("You ran out of guesses")
        if(letter in self.previous_guesses):
            raise Exception("You've already guessed this letter")
        self.previous_guesses.add(letter)
        found = False
        for w in range(len(self.word)):
            if(self.word[w] == letter):
                self.state[w] = letter
                found = True
        if(not found):
            self.incorrect_guesses.append(letter)
            return False, "Incorrect Guess"



        pass

class Game:
    def __init__(self, words_fiile):
        if(words_fiile):
            self.words = read_words(words_fiile)
        else:
            raise FileNotFoundError("Please input a file")
    



    

        
