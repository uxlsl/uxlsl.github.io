---
layout: post
title: pytest-fixture学习笔记
category: 学习
keywords: 学习,2015
---


> The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute. pytest fixtures offer dramatic improvements over the classic xUnit style of setup/teardown functions:

>  fixtures have explicit names and are activated by declaring their use from test functions, modules, classes or whole projects.
>    fixtures are implemented in a modular manner, as each fixture name triggers a fixture function which can itself use other fixtures.
>    fixture management scales from simple unit to complex functional testing, allowing to parametrize fixtures and tests according to configuration and component options, or to re-use fixtures across class, module or whole test session scopes.

注:
测试夹具目的是提供一个固定的装置能够可靠地重复地执行.pytest的测试夹具提供不同的方法去实现 Xunit风格的启动和关闭(setup/teardown).

1. 夹具有明确的名字,能够通过声明在函数,模块,整个项目中使用激活.
2.
3. 夹具管理模式能够使用不同配置和选项从而在简单,复杂的函数进行测试.


# 功能分析

1. pytest.fixture参数

scope > module, session ,function

    + module 指在每一次模块中执行一次
    + session 指在会话中执行一次
    + function 指在每个函数中执行一次

params > 类型列表,每一个是一次参数.


2. 装饰后的fixture函数的request参数
request

    + params   显而易见是参数
    + addfinalizer 结束时执行

3. @pytest.mark.usefixtures(fixturename)
标注class使用什么fixture


```


import os
import pytest

@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []

```

4. 配置文件

```

# content of pytest.ini
[pytest]
usefixtures = cleandir # 每个模块都会执行一次!


```

# fixture 的一个库factory_boy

> As a fixtures replacement tool, it aims to replace static, hard to maintain fixtures with easy-to-use factories for complex object.

目标是代替静态,难于维护的fixture,从而对于复杂的对象容易使用.

# 测试代码目录

demo/2015-12-14/pytest-fixture
