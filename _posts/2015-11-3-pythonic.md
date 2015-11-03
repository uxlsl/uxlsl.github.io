---
layout: post
title: pythonic的一些理解
category: python
keywords: 阅读,2015
---


#　如何看待pythonic
> Moreover, when a veteran Python developer (a Pythonista) points to portions of code and says they are not “Pythonic”,
> it usually means that these lines of code do not follow the common guidelines
> and fail to express the intent in what is considered the best (hear: most readable) way.

可以看出成功pythonic 的条件有
+ 按照公共的指南
+ 高可读性

## 习惯用法
+ 解包/拆包

`
    for index, item in enumerate(some_list):
    # do something with index and item
`

+ 文件的读取

`
    with open('/etc/passwd', 'rb') as f:
        # do something
`

+ 列表推导

`
    [ i for i in range(100) if i % 2 or i % 5 ]
`

+ 迭代

`
    for i in range(100):
        do some thing

`


# 格言

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never. (马上行动)
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
