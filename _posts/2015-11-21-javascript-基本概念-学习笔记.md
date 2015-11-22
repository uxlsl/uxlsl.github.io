---
layout: post
title: javascript 基本概念笔记
category: 学习
keywords: 学习,2015
---

# javascript 基本概念笔记

## 变量

原则:
+ 基本类型是复制.
+ 对象是引用.
+ 没有块级结构.
+ 函数参数不用指定类型.
+ 全局变量


*对象* 引用
![对象引用](http://7xnnj6.com1.z0.glb.clouddn.com/javascript-var.jpg)

这就好像A,B喜欢C,然后A喜欢D,但不能改变B喜欢C.

### 优化
尽可能不用的变量,给null


### 作用域
函数,作用于定义后面的函数.


## 函数

+ 没有重载.
+ 没有缺省参数.
+ 也可访问arguments来查看参数.
+ 检查参数不严格.


## 执行环境

### 函数

this可以说是当前的执行环境.


```

window.color = "red";
var o = {color: "blue"};

function sayColor(){
    alert(this.color);
}

o.sayColor = sayColor();

o.sayColor();


with(o){
    alert(color);
}

```




# 参考

javascript高级编程.
