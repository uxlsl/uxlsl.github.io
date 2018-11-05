---
layout: post
title: 使用pycookiecheat提取网站对应的cookies
category: 学习
keywords: 学习,2018
---


# 使用pycookiecheat提取网站对应的cookies

前提条件:

+ chrome


```

In [1]: from pycookiecheat import chrome_cookies
   ...:
   ...: url = 'https://www.douban.com/'
   ...: cookies = chrome_cookies(url)

In [2]:

In [2]: cookies
Out[2]:
{'bid': 'g1ytdqjYBAc',
 'douban-fav-remind': '1',
 'll': '"118281"',


```

## 结论
可以轻松提取浏览器对应网站的cookies
