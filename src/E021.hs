{--
Get the sum of all amicable numbers under 10000
OPTIMAL (<0.1 s) 

APPROACH:
    Brute force approach. Check the sum of all the factors and then make sure
    than the sum is equal to the starting number. 
-}

import Helpers (getProperFactors)

limit :: Int
limit = 10000

sumFactors :: Int -> Int
sumFactors = sum . getProperFactors

getAllAmicable :: [Int]
getAllAmicable = foldl getAmicablePair [] [2..limit]
    where 
    getAmicablePair :: [Int] -> Int -> [Int]
    getAmicablePair xs n
        | sumFactorsOfN > n && isAmicableWithN sumFactorsOfN = n : sumFactorsOfN : xs 
        | otherwise = xs
        where
        sumFactorsOfN = sumFactors n
        isAmicableWithN x = sumFactors x == n

result :: Int
result = sum getAllAmicable

main :: IO ()
main = print result