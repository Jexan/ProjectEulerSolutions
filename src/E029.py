# N of Distinct powers a**b with 2 <= a <= 100, 2 <= b <= 100
# OPTIMAL (<0.1 s)
# 
# APPROACH:
#   Brute force. Use sets to assure uniqueness. 

result = len(frozenset(a**b for a in range(2, 101) for b in range(2, 101))) 