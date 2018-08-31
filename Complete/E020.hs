{--
Get the sum of the digits of factorial of 100.
OPTIMAL

APPROACH:
    See E020.py.
--}

import Helpers (factorial, sumOfDigits) 

limit :: Int
limit = 100

result :: Int
result = sumOfDigits $ factorial limit

main = do
    print result