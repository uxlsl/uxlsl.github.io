---
layout: post
title: 使用cookiecutter快速建python包
category: 学习
keywords: 学习,2018
---

# 建包的好处

1. 能够复用成果，不用造轮子



# 建包方法

1. 编写setup.py(往往很重复)
2. README.rst|README.md
3. LICENSE

总之比较无聊写这些 ,有识之仕也看到这一点,于是写了，cookiecutter，并写了生成python包的方法
*这样*

```

pip install cookiecutter
git clone https://github.com/kragniz/cookiecutter-pypackage-minimal.git
cookiecutter cookiecutter-pypackage-minimal/

```

你要做的是在源代码目录上修改即可

