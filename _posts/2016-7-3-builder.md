
---
layout: post
title: 致自己曾经学习的知识－生成器模式
category: 学习
keywords: 学习,2016
---


## 定义
把对象的构建与表现分离，使得同样的构建过程能创建不同的表示


## 参于对象

对象 builder
对象构建 director


## python 实现例子


```

# Director
class Director(object):

    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


# Abstract Builder
class Builder(object):

    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError

# Concrete Builder
class BuilderHouse(Builder):

    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


class BuilderFlat(Builder):

    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'


# Product
class Building(object):

    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)


```


## 总结

1. 分离
2. 实现就是
3. 继承实现抽象
