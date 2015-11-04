---
layout: post
title: pythonic的一些理解
category: python
keywords: 阅读,2015
---

# pythonic 是什么？
pythonic 有点像，idiomatic Python
*很python*, 其实就是python的惯用和特有写法。

> Pythonic means code that doesn't just get the syntax right but that follows the conventions of the Python community and uses the language in the way it is intended to be used.[what-does-pythonic-mean](http://stackoverflow.com/questions/25011078/what-does-pythonic-mean)


#　如何看待pythonic

> Moreover, when a veteran Python developer (a Pythonista) points to portions of code and says they are not “Pythonic”,
> it usually means that these lines of code do not follow the common guidelines
> and fail to express the intent in what is considered the best (hear: most readable) way.

可以看出成功pythonic 的条件有
+ 按照公共的指南
+ 高可读性

# 相关评论

> 编写高质量代码：改善Python程序的91个建议
> 看起来就像伪代码。

> 在经验老到的 Python 程序员看来，不够 Pythonic 的代码往往看起来古怪而且累赘，过于冗余也难以理解。因为它使用冗长的代码代替常见的、公认的、简短的惯用法来实现预期效果。更甚于此的是在语言支持正确的惯用法之后，非推荐的代码通常执行起来更慢。

> Pythonic 就是以清晰、可读的惯用法应用Python 理念和数据结构。举个例子，应该多使用动态类型，在无必要之处引入静态类型就走向了另一端。另外也要避免使用经验丰富的 Python 程序员不熟悉的方式去完成任务（即遵循最小惊奇原则）。[Pythonic到底是什么玩意儿？](http://blog.csdn.net/gzlaiyonghao/article/details/2762251)

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


# 参考

(pep8)[https://www.python.org/dev/peps/pep-0008/]
