---
layout: post
title: 使用functools-lru_cache进行数据缓存
category: 学习
keywords: 学习,2016
---


## 使用functools-lru_cache 进行缓存



@functools.lru_cache(maxsize=128, typed=False)

If maxsize is set to None, the LRU feature is disabled and the cache can grow without bound. The LRU feature performs best when maxsize is a power-of-two.

If typed is set to True, function arguments of different types will be cached separately. For example, f(3) and f(3.0) will be treated as distinct calls with distinct results.

当 maxsize 设置为None,缓存将会是所有参数
当 typed 设置为 True,不同的类型将会被认为分在不同的缓存



```

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

>>> [fib(n) for n in range(16)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

>>> fib.cache_info()
CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)


```
