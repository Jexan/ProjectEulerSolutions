{-- 
Get the numbers -1000 < a, b < 1000 such that n^2 + a*n + b produces more
consecutive primes.
OPTIMAL

APPROACH: 
    See E027.py. 
--}

import Helpers (getPrimesUntil)
import qualified Data.IntSet as IntSet

possibleA :: IntSet.IntSet
possibleA = IntSet.fromAscList [-999, -997.. 1000]

possibleB :: IntSet.IntSet
possibleB = IntSet.union primes $ IntSet.map negate primes

primes :: IntSet.IntSet
primes = IntSet.fromAscList $ getPrimesUntil 1000

possibleCombinations :: [(Int, Int)]
possibleCombinations = cartesianProduct possibleA possibleB

maxCombination :: (Int, Int)
maxCombination = head $ fst $ highestPrimesCombination (possibleCombinations, 1) 
    where
    highestPrimesCombination :: ([(Int, Int)], Int) -> ([(Int, Int)], Int)
    highestPrimesCombination (possible, n) 
        | length possible == 1 = (possible, n)
        | otherwise = highestPrimesCombination (getsPrime possible, n + 1)
        where 
        getsPrime :: [(Int, Int)] -> [(Int, Int)]
        getsPrime = filter (\(a, b) -> IntSet.member (abs squareN + a*n + b) primes)  

        squareN :: Int
        squareN = n*n

cartesianProduct :: IntSet.IntSet -> IntSet.IntSet -> [(Int, Int)]
cartesianProduct a b = concat $ map (\i -> zip (repeat i) $ IntSet.elems b) $ IntSet.elems a 

result :: Int
result = fst maxCombination * snd maxCombination

main :: IO ()
main = print result