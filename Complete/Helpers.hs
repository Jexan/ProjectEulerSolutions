module Helpers (
    getPrimesUntil,
    getProperFactors,
    factorial,
    sumOfDigits,
    hasCommon
) where

import qualified Data.IntMap as Map
import Data.Char (digitToInt)

type Sieve = Map.IntMap Bool

hasCommon :: Eq a => [a] -> [a] -> Bool
hasCommon [] b = False
hasCommon (a:as) b
    | elem a b = True
    | otherwise = hasCommon as b 

getPrimesUntil :: Int -> [Int]
getPrimesUntil n = 2 : (filter (\k -> Map.lookup k sieve == Just True) $ Map.keys sieve)
    where
    sieve = sieveUntil n

sieveUntil :: Int -> Sieve
sieveUntil n = foldl popSieve Map.empty [3, 5 .. n]
    where 
    isSieved :: Sieve -> Int -> Bool 
    isSieved sieve n =
        case Map.lookup n sieve of 
            Just False -> False
            Nothing   -> True 

    popSieve :: Sieve -> Int -> Sieve
    popSieve sieve from = if prime
        then foldl (\sieve n -> Map.insert n False sieve) updatedSieve [start, start+from .. n]
        else sieve
        where 
        prime = isSieved sieve from 
        start = from ^ 2
        updatedSieve = if prime then Map.insert from True sieve else sieve 

getProperFactors :: Int -> [Int]
getProperFactors n = 1 : foldl concatDivisors [] [2 ..  floor $ sqrt $ fromIntegral n]
    where
    concatDivisors :: [Int] -> Int -> [Int]
    concatDivisors xs m 
        | mod n m == 0 = (if m == division then id else (:) division) $ m : xs
        | otherwise = xs
        where division = div n m

factorial :: Integer -> Integer
factorial n = fromIntegral $ product [1..n]

sumOfDigits :: Integer -> Int
sumOfDigits = sum . map digitToInt . show