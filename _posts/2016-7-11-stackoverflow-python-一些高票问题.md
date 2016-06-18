---
layout: post
title: stackoverflow-python的一些高票问题
category: 学习
keywords: 学习,2016
---


## what's the difference between the list methods append and extend?(列表的append和extend方法的区加)


## 回答

append: append object at end
append: 将对象放在尾部

```

x = [1, 2, 3]
x.append([4,5])
print(x)


```
gives you: [1, 2, 3, [4, 5]]
结果:[1,2,3,[4,5]]

extend: extend list by appending elements from iterable!
extend: 扩展列表通过一个个地放到尾部

```

x = [1, 2, 3]
x.extend([4,5])
print(x)

```

gives you: [1, 2, 3, 4, 5]
结果:[1,2,3,4,5]


## iterating over dictionaries using for loops in Python?(python迭代字典使用for)

key is just a variable name.
key 只是一个变量的名字而已。
for key in d: will simply loop over the keys in the dictionary, rather than the keys and values. To loop over both key and value you can use the following:
for key in d: 只是简单地循环字典的关键字而已, 比如关键字和值，　循环关键字和值，你可以使用下面的方法.

Edit

For Python 2.x-
对于 python 2.x时,使用这个

for key, value in d.iteritems():

For Python 3.x-
对于 python 3.x时,使用这个
for key, value in d.items():

Test for yourself, change the word key to poop.

Explanation-
解释

For Python 3.x, iteritems() has been replaced with simply items(), which returns a set-like view backed by the dict, like iteritems() but even better. This is also available in 2.7 as viewitems(). The operation items() will work for both 2 and 3, but in 2 it will return a list of the dictionary's (key, value) pairs, which will not reflect changes to the dict that happen after the items() call. If you want the 2.x behavior in 3.x, you can call list(d.items()).

对于python3.x, iteritems()已经被items取代了，它将会返回像字典的视图，　items()方法在python2和python3都能正常工作，但python2 是返回一个列表的健和值对，这个不会影响字典当调用了items()之后,如果你想2.x 和 3.x 行为一样，你可以调用 list(d.items())



## 参考

http://stackoverflow.com/questions/252703/append-vs-extend/252711#252711
http://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops-in-python/3294899#3294899
