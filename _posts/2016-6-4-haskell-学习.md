---
layout: post
title: haskell学习
category: 学习
keywords: 学习,2016
---


## haskell学习

关于列表小结：
头连接使用(常用)
x:xs
如:
1:[2,3]

尾连接

++ 连接符
[1] ++ [1, 3]
[1, 1, 3]

无尽函数
[1..]

take 12 [1..]
takeWhile (<12) [1..]

## 应用

定义反转列表


```

reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = reverse' xs ++ [x]


```

取数后反转列表

```

(reverse' takeWhile (<12) [1..])

```


