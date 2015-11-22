---
layout: post
title: javascript 对象笔记
category: 学习
keywords: 学习,2015
---


# javascript 对象笔记

+ 属性
+ 方法

**奇怪**
定义对象像定义字典.

```

var persion = {"name":"bar",
               "age": 22,
               "job": "7lk"};

```


## 属性

### 设置可写性,也许在严格模式中有效.



```

Object.defineProperty(persion, "help",{
  writable: false,
  value:"my book"
});

```

### 动态设置属性

```

Object.defineProperty(XX, name, {get:XX,set:XX})

```

## 构造函数形式

```

function Persion(name, age, job){
  this.name = name;
  this.age = age;
  this.job = job;
};

```

### 原型模式

```

function Persion(){
}

Persion.prototype.name ="lsl";
Persion.prototype.age = 100;
Persion.prototype.job = "7lg";

```


## TODO

1. 继承


## 参考
javascript 高级编程.
