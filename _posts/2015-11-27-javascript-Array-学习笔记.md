---
layout: post
title: javascript-Array-学习笔记
category: 学习
keywords: 学习,2015
---

# javascript-Array-学习笔记
![](http://7xnnj6.com1.z0.glb.clouddn.com/javascript-Array.jpg)
![](http://7xnnj6.com1.z0.glb.clouddn.com/javascript-Array2.jpg)

+ slice 切片 是返回新数组,注意检测长度,因为切长度大于原长度时不会报错
+ sort|reverse 是原地排序,要注意是否想原地排序
+ pop 出来如果为空是出undefined
+ length 能给值,从而长度变短了
+ join,tostring,valveof 转字符串
+ every some,map,filter,forEach 都会给每个成员进行调用,但返回结果不同
  every some,是对整个数组测试,filter是对数组过滤,map,是保存每次函数的结果组成的值,forEach是没有返回结果


# 例子

```
// 以下使用了nodejs解释器

> var a=new Array()
undefined
> a
[]
> Array.isArray(a)
true
> for(var i=0;i< 10;i++){
... a[i]=i;
... }
9
> a
[ 0,
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9 ]

> a.slice(0,3)
[ 0, 1, 2 ]
> a.every(function(v){
... return v > 0;})
false
> a.some(function(v){
... return v > 0;})
true
> a.shift()
0
> a
[ 1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9 ]
> a.pop()
9
> a.push(10)
9
> a
[ 1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  10 ]
> a.reverse()
[ 10,
  8,
  7,
  6,
  5,
  4,
  3,
  2,
  1 ]


```
