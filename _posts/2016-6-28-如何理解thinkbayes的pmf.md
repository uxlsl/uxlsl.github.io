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

## 蒙帝问题
问题大概是这样的有三对门，将一台车放在门后，你选择一个门称为A，
蒙帝就会打开其他一个门，然后问你是否重新选择？
解：
车能放在任何一对门，可能性一样

因此初始化就是这样

```

        Pmf.__init__(self)
        for hypo in hypos:
            self.Set(hypo, 1)
        self.Normalize()


```

计算likelihood
如果车在A, B, C,哪么概率1/2,0,1

车在A后， B,C都能打开，
车在B后, B不可能打开， 概率为0, 只能打开C
车在C后, B打开， 概率为1, 只能打开B

```

        if hypo == data:
            return 0
        elif hypo == 'A':
            return 0.5
        else:
            return 1


```

结果
A 0.333333333333
B 0.0
C 0.666666666667

## 豆豆问题

列举所有情况
A 袋子1， 1994，袋子2， 1996
B 袋子1， 1994，袋子2， 1996

```

suite = M_and_M('AB')

```

计算似然度， 先豆后豆

```

    suite.Update(('bag1', 'yellow'))
    suite.Update(('bag2', 'green'))

```

A 0.740740740741
B 0.259259259259


## 参考
[thinkbayes](http://greenteapress.com/wp/think-bayes/)
