{--
Champernowne const = 0.12345678910111213...

If d n represents the n th digit of the Champernowne's, find the value of the following expression.
d 1 × d 10 × d 100 × d 1000 × d 10000 × d 100000 × d 1000000  
OPTIMAL(<0.1s)

APPROACH:
    Brute force. Create a string of the numbers and just get the digits asked and use product.

--}

import Data.Char (digitToInt)

champernowne :: String
champernowne = concat $ map show [1..]

digitsNum :: [Int]
digitsNum = map (\n -> digitToInt $ champernowne !! (n - 1)) milestoneNums

milestoneNums :: [Int]
milestoneNums = map (10^) [0..6]

result :: Int
result = product digitsNum

-- 210
main :: IO ()
main = print result