---
layout: post
title: python sorted 笔记
category: python
keywords: 学习,2015
---

# python sorted笔记

数据:
data = [
{
'name':'foo',
'age': 23,
'job': 'banana',
},
{
'name':'bar',
'age': 54,
'job': 'watermelon',
},
{
'name':'xx',
'age': 35,
'job': 'apple',
},
]

问题:
1. 按name排序
2. 按name, age,排序
3. 按name,age, job排序

解决方案使用
sorted
key参数说明: 返回了一组比较序列.
operator.itemgetter返回拿属性的值
例子:
itemgetter('name','age')(data[0]) -> ['foo', 2]

由此看来适合做sorted的key

1. sorted(data, key=itemgetter('name'))
-> [{'age': 54, 'job': 'watermelon', 'name': 'bar'},
 {'age': 23, 'job': 'banana', 'name': 'foo'},
 {'age': 35, 'job': 'apple', 'name': 'xx'}]

2. sorted(data, key=itemgetter('name', 'age'))
->
[{'age': 54, 'job': 'watermelon', 'name': 'bar'},
 {'age': 23, 'job': 'banana', 'name': 'foo'},
 {'age': 35, 'job': 'apple', 'name': 'xx'}]


3. sorted(data, key=itemgetter('name', 'age', 'job'))
->
[{'age': 54, 'job': 'watermelon', 'name': 'bar'},
 {'age': 23, 'job': 'banana', 'name': 'foo'},
 {'age': 35, 'job': 'apple', 'name': 'xx'}]

*注意*
要明确看出结果的区别,则要数据要改进.
