{--
How many n-digits numbers that are a nth power?
OPTIMAL

APPROACH:
    All the numbers that fit the criteria must be created from a base lesser than 10
    (since 10^n, the lower bound, has 2n digits for n > 0). 

    Also, if n^m has m+1 digits, n^(m+1) will have m+2 or m+1 digits. 
        In the first case n^x will just fall behind.
        In the second case, there's hope, but if the n^(m+1) still has only m digits, there's nothing to do.
--}

numberOfNthPowers :: Integer
numberOfNthPowers = produceNumbers 1 1
    where
    produceNumbers :: Integer -> Integer -> Integer
    produceNumbers 10 _ = 0
    produceNumbers base digits
        | lowerBound <= result && result < maxBound = 1 + checkNumberNextDigit
        | otherwise = if result * base < lowerBound then checkNumberNextBase else checkNumberNextDigit
        where
        lowerBound :: Integer
        lowerBound = 10 ^ (digits - 1)

        maxBound :: Integer
        maxBound = lowerBound * 100

        result :: Integer
        result  = base ^ digits

        checkNumberNextDigit :: Integer
        checkNumberNextDigit = produceNumbers base $ digits + 1

        checkNumberNextBase :: Integer
        checkNumberNextBase = produceNumbers (base + 1) 1 

-- 49
result :: Integer
result = numberOfNthPowers

main :: IO ()
main = print result