---
layout: post
title: django model操作总结
category: python
keywords: 学习,2015
---


# django 复杂查询总结
何谓复杂查询?
就是不能通过简单的查询来达到目的.
django 来说就是条件全部与,然后得结果.

在sql哪些>=,<=, like,%, and, or,==,
(x and y) or (z and v)

## like


## Q


```

from django.db.models import Q
Q(question__startswith='What')
Q(question__startswith='Who') | Q(question__startswith='What')
Q(question__startswith='Who') | ~Q(pub_date__year=2005)


```

Q可以说是应 and,or,not 查询如生,
如上面例子不用 |,基本上写不出一行来表达这样的意思.



## 如何检查生成sql是否符合要求.

print Foo.objects.all().query
