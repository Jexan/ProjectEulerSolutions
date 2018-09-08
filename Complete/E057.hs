{--
Square root expansion with numerators bigger than denominator.
SLOW (~5 s)

APPROACH:
    Basically brute force. 
--}

import Data.Ratio

limit :: Int
limit = 1000

fitsCriteria :: Rational -> Bool
fitsCriteria a = (length $ show $ numerator a) > (length $ show $ denominator a)

partialSums :: [Rational]
partialSums = iterate (\n -> 2 + 1 / n) (2 % 1)

yieldTerms :: [Rational] 
yieldTerms = map (\n -> 1 + 1/n) (2 : partialSums)

result :: Int
result = length $ filter fitsCriteria $ take limit yieldTerms

-- 153
main :: IO ()
main = print result