# name score of p022 based of alphabetical order

import os

FILE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'p022_names.txt')

def get_scores_of_names():
    acc = 0
    with open(FILE_DIR, 'r') as f:
        content = f.read().replace('"', '').replace('\n', '').split(',')
        content.sort()
        
        for index, name in enumerate(content):
        	acc += (index+1) * get_alpha_score(name)

    return acc

def get_alpha_score(n):
    return sum([ord(i) - 64 for i in n])

assert(get_alpha_score('COLIN') == 53)
result = get_scores_of_names()