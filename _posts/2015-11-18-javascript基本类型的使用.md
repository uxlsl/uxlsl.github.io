---
layout: post
title: javascript 基本类型的使用
category: 学习
keywords: 学习,2015
---


# javascript 基本类型的使用
+ RegExp

## RegExp
创建RegExp,可以使用类似perl的写法
var expression = / pattern / flags;
flags g,i,m
这种是共享了一个实例,
新的实例,new RegExp("cat", "g")


### 方法

RegExp 对象.test
RegExp 对象.exec


### 实例

```
var exp = /.at/g
var exp = /lo/
var exp = /(lo)/gi
var exp = /(lo)/gim


```
