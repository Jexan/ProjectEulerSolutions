{--
How many circular primes are there under 1000000?
SLOW (~9 s)

Approach:
    Basically Brute Force the way through.
    Check all the primes that are circular from 1 to 1000000.
    We know that if the prime has the digits 0,2,4,6,8, 
    and remove circular permutations that are not quite circular.
-}

import Helpers (getPrimesUntil, hasCommon)
import qualified Data.IntSet as IntSet

limit :: Int
limit = 1000000

primes :: IntSet.IntSet
primes = IntSet.fromAscList $ filter (\p -> not $ hasCommon "02468" $ show p) $ getPrimesUntil limit

circularize :: Int -> [Int]
circularize n = map read $ take (length strN) $ iterate cycleN strN 
    where
    strN :: String
    strN = show n

    cycleN :: String -> String
    cycleN (x:xs) = xs ++ [x] 

nCircularPrimes :: Int
nCircularPrimes = IntSet.size $ circularPrimes primes IntSet.empty 
    where
    circularPrimes :: IntSet.IntSet -> IntSet.IntSet -> IntSet.IntSet
    circularPrimes primesSet circularSoFar 
        | IntSet.null primesSet = circularSoFar
        | otherwise = circularPrimes updatedPrimes updatedCircular
        where
        circularList :: [Int]
        circularList = circularize prime

        prime :: Int
        prime = head $ IntSet.elems primesSet
       
        circularPossibilities :: IntSet.IntSet
        circularPossibilities = IntSet.fromList circularList 

        isCircular :: Bool
        isCircular = all (\p -> IntSet.member p primesSet) circularList

        updatedPrimes :: IntSet.IntSet
        updatedPrimes = IntSet.difference primesSet circularPossibilities 

        updatedCircular :: IntSet.IntSet
        updatedCircular
            | isCircular = IntSet.union circularSoFar circularPossibilities
            | otherwise = circularSoFar

-- 2 is shafted in the initial filtering
result :: Int
result = nCircularPrimes + 1

main :: IO ()
main = print result