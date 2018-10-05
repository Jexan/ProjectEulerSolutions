{--
Get the last ten digits of the non-Mersenne Prime 28433*2^7830457 + 1  
NORMAL (<2s)

APPROACH
    Just calculate the Mersenne prime. It works quite fast and it's easy.
--}

getLastDigits :: Integer -> Integer -> Integer
getLastDigits n digits = mod n (10 ^ digits)
   
nonMersennePrime :: Integer 
nonMersennePrime = 28433 * 2^7830457 + 1

-- 8739992577
main :: IO ()
main = print $ getLastDigits nonMersennePrime 10