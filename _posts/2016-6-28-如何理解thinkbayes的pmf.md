---
layout: post
title: 如何理确thinkbayes的pmf
category: 学习
keywords: 学习,2016
---

## 如何理确thinkbayes的pmf

首先先看看贝叶斯表达式

中文是这样的
先验概率*似然度／标准化常量


```

from thinkbayes import Pmf

pmf = Pmf()
pmf.Set('Bowl 1', 0.5) # 设置先验概率
pmf.Set('Bowl 2', 0.5)

pmf.Mult('Bowl 1', 0.75) # 乘于似然度
pmf.Mult('Bowl 2', 0.5)

pmf.Normalize() # 归一化

print pmf.Prob('Bowl 1')

```

就这样能理确否？
