# How many Triangle words in text file?
# OPTIMAL 

import os
from math import floor

def get_alpha_score(n):
    return sum(ord(i) - 64 for i in n)

def triangular(n):
    return floor(n*(n+1)/2)

def get_triangular_words():
    with open(FILE_DIR, 'r') as f:
        content = f.read().replace('"', '').replace('\n', '').split(',')

    return len(tuple(i for i in content if get_alpha_score(i) in tri_ns))

FILE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'p042_words.txt')
tri_ns = frozenset(map(triangular, range(35)))

DUMMY_WORD = 'SKY'

assert get_alpha_score(DUMMY_WORD) in tri_ns
result = get_triangular_words()