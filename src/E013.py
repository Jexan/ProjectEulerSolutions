# Sum of the numbers of every line
# OPTIMAL (<0.1s)
# 
# APPROACH:
#   Sum the parsed digits of the string. Basically brute force.

import os

FILE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'p013_number.txt')

with open(FILE_DIR ,'r') as f:
    result = int(str(sum( int(n) for n in f.read().split('\n') ))[:10])