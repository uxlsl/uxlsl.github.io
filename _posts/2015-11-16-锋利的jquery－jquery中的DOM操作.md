---
layout: post
title: 锋利的jquery-jquery的DOM操作
category: 学习
keywords: 学习,2015
---


# 锋利的jquery-jquery的DOM操作
+ 创造节点
+ 插入节点
+ 复制节点
+ 删除节点
+ 属性操作
+ 样式操作
+ 文本与值
+ 遍历节点

## 创造节点
1. 通过html代码来创造节点
2. 创造出来的节点是不在文档上的,这时就要

## 插入节点
1. 位置的考虑, 在节点前还是后,成为child
2. 插入一个还是多个.

## 复制节点

1. 复制出来的属性是否和原来相同, 指一些原来的事件绑定.
2. 选择出来是多个怎么办?答案是隐式操作多个.

$("xx").clone(Ture/False);
True则原来事件绑定,数据还是存在的,
False则原来事件绑定,数据不存在了,


## 删除节点
1. 删除这个节点,还可以再次使用吗?

+ remove 删除匹配的节点,但能再次使用,但事件,附加数据不存在,前提你还有变量指向它.
+ detach 删除匹配的节点,但能再次使用,但事件,附加数据存在.前提你还变量指向它.
+ empty 清空这个节点,及其后代.


## 属性操作
attr(val);
val为值时,是查询,为字典时,则为更新属性.
removeAttr(val);


## 样式操作
+ 查询样式,attr
+ 设置样式,attr
+ 追加样式,addClass
+ 切换样式,toggleClass


## 文本与值
+ html
+ val 一般指表格提交.
+ text

# 遍历节点
1. children()
2. next()
3. pre()
4. siblings()
5. parent()
6. parents()
7. closest()


# 参考
[1:锋利的jquery
