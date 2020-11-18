import os
def read_words():
    '''
    Input: file: file
    Output: words: list
    '''
    with open('words.txt') as f:
        flat_list=[word for line in f for word in line.split()]
    del flat_list[:2]
    return flat_list
