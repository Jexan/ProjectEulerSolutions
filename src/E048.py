# Find the last ten digits of the series, 1 1 + 2 2 + 3 3 + ... + 1000 1000 
# OPTIMAL(<0.2s)
# 
# APPROACH:
#   Brute force approach. It works well enough so why change it?

result = int(str(sum(i**i for i in range(1, 1001)))[-10:])