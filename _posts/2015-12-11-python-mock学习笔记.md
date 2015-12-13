---
layout: post
title: python mock 学习总结
category: 学习
keywords: 学习,2015
---

> 馀分闰位，谓以伪乱真耳。 <颜氏家训>

> unittest.mock is a library for testing in Python. It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

unittest.mock 是python测试的一个库,它能让你在测试是代替系统的一部分,并且能使用断言它们是否有用过.


# 问题?

1. 用什么代替系统的一部分?
2. 如何代替?

答
1. MagicMock

> Mock and MagicMock objects create all attributes and methods as you access them and store details of how they have been used. You can configure them, to specify return values or limit what attributes are available, and then make assertions about how they have been used:

mock 和magicMock对象 能够任何属性和方法,并且能够记录它们是怎样使用的,你也能够配置它们返回指定属性.
和使用断言 它们是怎样使用的


2. mock.patch

> The patch decorators are used for patching objects only within the scope of the function they decorate. They automatically handle the unpatching for you, even if exceptions are raised. All of these functions can also be used in with statements or as class decorators.

patch 装饰器能够给指定作用城内给对象打补丁,并且过了作用城自动解除, 使用可以是with,or,类装饰.
(自动还原原来的好重要!)
方式:
1. @patch
2. patch.object
3. patch.start,patch.end
4. patch.dict ?

1. 适合在测试方法,并且只在这个方法使用.
2.
3. 适合通用情况,提取到 setUp, tearDowm,作公共方法
4. 适合改变一些字典,比如 os.environ


# 练习

----demo/code/2015-12-11/mocktest.py----

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

# 使用pathc装饰器形式!
@patch('module.hello')
def test(mock_hello):
    module.hello()
    assert mock_hello.called

test()

# 使用patch.object形式!
with patch.object(module, "hello", return_value=100) as mock_hello:
    module.hello()
    assert mock_hello.called



class MyTest(TestCase):
    def setUp(self):
        self.patcher1 = patch('module.hello')
        self.Mock_hello = self.patcher1.start()

    def tearDown(self):
        self.patcher1.stop()

    def test_something(self):
        assert module.hello is self.Mock_hello

MyTest('test_something').run()

# 使用patch.dict
foo = {}
with patch.dict(foo, {'newkey': 'newvalue'}):
     assert foo == {'newkey': 'newvalue'}

```


# 参考
[unittest](https://docs.python.org/3/library/unittest.mock.html?highlight=mock#module-unittest.mock)
