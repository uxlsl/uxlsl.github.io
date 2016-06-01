---
layout: post
title: haskell-函数练习
category: 学习
keywords: 学习,2016
---


## haskell  函数练习


计算收益

```

total_money :: Double -> Double -> Double -> Double
total_money a p y = let x = (1 + p) in a * x ** y

```

计算每月应该还


```


back_money total p n = let p1 = 1 + p in total * p1**n * ( 1 - p1) / ( 1 - p1**n )


```

计算绝对值

```

abs :: Integral a => a -> a

abs n | n > 0 = n
      | otherwise = -n

```


计算月有多少日


```

month' :: Int -> Int
month' 1 = 31
month' 2 = 28
month' 3 = 31
month' 4 = 30
month' 5 = 31
month' 6 = 30
month' 7 = 31
month' 8 = 31
month' 9 = 30
month' 10 = 31
month' 11 = 30
month' 12 = 31
month' _  = error "invalid month"


```
