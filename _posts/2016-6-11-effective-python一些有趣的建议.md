---
layout: post
title: effective-python一些有趣的建议
category: 学习
keywords: 学习,2016
---


## 注意参数是迭代类型

i 为迭代参数
参数为迭代类型的坏处是要不能使用二次，比如使用一次sum(i) 后不能使用第二次

例子：

```

def f(scores):
    total = sum(scores)
    return [i / total for i in scores]

print f(i for i in range(100))
# 结果为[]

```

如何解决

1.  在doc中声明不能为迭代类型， 但有时候不知不觉的用了而不知道，出现差错是很大理解是这个原因

2.  使用__iter__ ,但总觉得麻烦


```

class ReadVisits(object):
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path) as f:
            for line in f:
                yield line

def f(scores):
    if iter(scores) is iter(scores):
        raise TypeError('xxx')
    total = sum(scores)
    return [i / total for i in scores]


f(ReadVisits('/etc/passwd'))


```


## mix-in组件

注意mixin实现
注意制作mixin组件
注意classmethod的使用

```

import json


class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class JsonMixin(object):
    @classmethod
    def from_json(cls, data):
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        return json.dumps(self.to_dict())

class BinaryTree(ToDictMixin, JsonMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = BinaryTree(10,
        BinaryTree(1),
        BinaryTree(2))

print tree.to_dict()
print tree.to_json()


```
