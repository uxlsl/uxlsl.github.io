
# -*- coding:utf-8 -*-
"用来学习如何使用mock"
import sys
from unittest import TestCase
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
    assert mock_hello == module.hello
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



foo = {}
with patch.dict(foo, {'newkey': 'newvalue'}):
     assert foo == {'newkey': 'newvalue'}


