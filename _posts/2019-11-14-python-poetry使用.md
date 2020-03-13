---
layout: post
title: 2019-11-14-python-poetry使用.md
category: 学习
keywords: 学习,2019
---

# 安装

安装建议
```

curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

```

如果太慢

```

pipx install poetry

```

注pipx 在隔离环境中安装和运行 Python 应用


# 使用


1.  新建项目

``` 

poetry new project 

```

2. 安装信赖包

``` 

poetry install

```

3. 增加包 比如

```

poetry add requests pendulum

```

4. 显示依赖


```

poetry show 

```
