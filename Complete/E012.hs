{--
First triangular number with more than 500 divisors.
SLOW (~14 s)

APPROACH:
    Brute force approach. Just generate the triangular numbers and
    check every one of them.
--}

import Helpers (getProperFactors)
import Data.List (find)
import Data.Maybe (fromJust)

limit :: Int
limit = 500

dummyLimit :: Int
dummyLimit = 5

dummyResult :: Int
dummyResult = 28

nFactors :: Int -> Int
nFactors n = 1 + (length $ getProperFactors n) 

triangularNumbers :: [Int]
triangularNumbers = scanl1 (+) [1..] 

firstTriangularWithNDivisors :: Int -> Int
firstTriangularWithNDivisors n = fromJust $ find (\triangular -> n <= nFactors triangular) triangularNumbers

checkCondition :: IO ()
checkCondition
    | dummyResult /= firstTriangularWithNDivisors dummyLimit = error "Bad condition"
    | otherwise = return () 

result :: Int
result = firstTriangularWithNDivisors limit

main :: IO ()
main = do 
    checkCondition
    print result