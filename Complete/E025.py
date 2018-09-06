# First fibonacci number with more than 1000 digits
# OPTIMAL (<0.1s)
# 
# APPROACH:
#   It makes use of a very cute formula:
#   
#   Fn = round(phi**n/sqrt(5))
# 
#   Since it is a monotonic continuos function, we can get an approximate of n, using the inverse function.
#   
#   In that case, we just check both the ceiling and floor of n. We have that
#   
#   F_floor(n) <= limit < F_ceil(n)
#   
#   So we check and return F_floor(n) if it is equal to the limit. Or we return the ceil.

from math import log, sqrt, ceil, floor
from decimal import Decimal  

LIMIT = Decimal(10.0) ** Decimal(999)

DUMMY_LIMIT = Decimal(100)
DUMMY_RESULT = 12

phi = Decimal(.5) + Decimal(5).sqrt() / Decimal(2)

def get_n_fibb(n):
    return round((phi ** n)/ Decimal(5).sqrt())

def fibonacci_greater_index(limit):
    sqrt5 = Decimal(5).sqrt()
    limit = sqrt5 * Decimal(limit)
    approx_n = limit.ln() / phi.ln()

    lowest_in, biggest_in = floor(approx_n), ceil(approx_n)
    
    if get_n_fibb(lowest_in) >= limit:
        return lowest_in
    else:
        return biggest_in

result = fibonacci_greater_index(LIMIT)
assert fibonacci_greater_index(DUMMY_LIMIT) == DUMMY_RESULT