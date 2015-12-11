---
layout: post
title: python mock 学习总结
category: 学习
keywords: 学习,2015
---

> unittest.mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

unittest.mock 是python测试的一个库,它能让你在测试是代替系统的一部分,并且能使用断言它们是否有用过.




# 练习


```

# -*- coding:utf-8 -*-
"用来学习如何使用mock"
from unittest.mock import *

# 示例1,主要是体现什么是mock
method = MagicMock(return_value=3)
print(method(3, 4, 5))
# 为了方便有 assert
method.assert_called_with(3, 4, 5)
# method.assert_called_with(3, 4, 6)

# 注意拼写错误, 打错在参数名不报错.
# 这样可以多次调用,返回不同的值.
mock = Mock()
mock.side_effect = [1, 2, 3, 4]
for i in range(4):
    print(mock())

mock = Mock(side_effect=[100])
print(mock())

# 与单元测试的关系.
from unittest.mock import patch
import module


@patch('module.hello')
def test(mock_hello):
    module.hello()
    assert mock_hello.called

# 使用patch.object形式!
with patch.object(module, "hello", return_value=100) as mock_hello:
    module.hello()
    assert mock_hello.called

test()

```
