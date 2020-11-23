import os
def read_words(file):
    '''
    Input: file: file
    Output: words: list
    '''
    with open(file) as f:
        flat_list=[word for line in f for word in line.split()]
    del flat_list[:2]
    return flat_list
