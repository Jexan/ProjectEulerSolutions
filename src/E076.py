# How many ways to express 100 with the sums of numbers below it
# OPTIMAL (<0.2s)
# 
# APPROACH:
#   Recurrency + functools.lru_cache for perfomance. Start with the sums,
#   making sure that any added number is not higher than the previous added numbers
#   (e.g. 5+4+... and not 4+5+... which are the same sum).

from functools import lru_cache

@lru_cache(None)
def reduce_num(to, current=0, max_in_chain=None):
    if to == current:
        return 1
    else:
        if not max_in_chain:
            max_in_chain = to - 1
        
        total = 0
        for i in range(1, min(to-current, max_in_chain) + 1):
            total += reduce_num(to, current+i, min(i, max_in_chain))

        return total

result = reduce_num(100)