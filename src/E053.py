# How many nCk with n <= 100 are greater than 1000000.
# OPTIMAL (<0.2s)
# 
# APPROACH:
#   Brute force approach. Since it is a very simple problem, there's no need for complications.

from .helpers import nCk

limit = 100
over = 1000000
counter = 0

for n in range(1, limit + 1):
    for k in range(2, n-1):
        if nCk(n, k) > over:
            counter += 1

result = counter