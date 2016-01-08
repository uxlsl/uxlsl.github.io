---
layout: post
title: ipython 的一些有用扩展
category: 学习
keywords: 学习,2016
---


# autoreload
自动重新reload 模块

%autoreload 0 关闭自动加载
%autoreload 1 配置加载自动加载的模块
%autoreload 2 配置加载不用自动加载的模块
%aimport 增加|删除自动加载的模块


```

In [1]: %load_ext autoreload

In [2]: %autoreload 2

In [3]: from foo import some_function

In [4]: some_function()
Out[4]: 42

In [5]: # open foo.py in an editor and change some_function to return 43

In [6]: some_function()
Out[6]: 43

```


# storemagic 存储一些变量

%store l
%store -r 恢复变量


# 配置文件


```

c.InteractiveShellApp.exec_lines = [
    'import numpy',
    'import scipy'
]
c.InteractiveShellApp.exec_files = [
    'mycode.py',
    'fancy.ipy'
    ]

```

# 总结
时常更新自已的日常操作,使自己与时俱.


# 参考
[autoreload](http://ipython.readthedocs.org/en/stable/config/extensions/autoreload.html)
[store](http://ipython.readthedocs.org/en/stable/config/extensions/storemagic.html)

# 自我检查
时间 2016-1-9,写下使用感受
