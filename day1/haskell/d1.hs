--valentin robert

pairs :: [a] -> [(a, a)]
pairs l = [(x, y) | (x : ys) <- tails l, y <- ys]

sumTo2020 :: (Integer, Integer) -> Bool
sumTo2020 (a, b) = a + b == 2020

solution :: [Integer] -> Integer
solution inputs =
  case find sumTo2020 (pairs inputs) of
    Nothing -> error "You promised there would be a pair that sums to 2020."
    Just (a, b) -> a * b
