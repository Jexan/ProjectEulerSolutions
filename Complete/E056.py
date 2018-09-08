# Get the max digit sum of a**b, a, b in [1, 99]
# NORMAL(<1.5s)
# 
# APPROACH:
#   Brute force the way through. Nothing smart.
#   
# NOTE:
#   Either the a or b that yields the max sum is 99. 

def get_digits():
    for a in range(2, 100):
        for b in range(2, 100):
            yield sum(int(i) for i in str(a**b))

result = max(get_digits())