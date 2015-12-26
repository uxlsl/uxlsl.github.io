---
layout: post
title: django-model 一些技巧
category: 学习
keywords: 学习,2015
---

# 使用模块法,简化模型结构

```

models -- __init__.py, People.py , city.py

__init__.py

from People import *
from city import *

People.py
from django.db import models

class XMan(models.Model):
....


```

# 使用模型继承简化模型的设计


```

class Postable(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = modified.DateTimeField(auto_now=True)
    message = models.TextField(max_length=500)

    class Meta:
        abstract = True


class Post(Postable):
    ...


class Comment(Postable):
...


```


# 参考

[模型](https://github.com/cundi/Django-Design-Patterns-and-Best-Practices/blob/master/%E7%AC%AC%E4%B8%89%E7%AB%A0-%E6%A8%A1%E5%9E%8B.md)
