---
layout: post
title: django-class-view学习
category: 学习
keywords: 学习,2015
---

# django-class-view 学习

> The relationship and history of generic views, class-based views, and class-based generic views
> In the beginning there was only the view function contract, Django passed your function an HttpRequest and expected back an HttpResponse. This was the extent of what Django provided.

> Early on it was recognized that there were common idioms and patterns found in view development. Function-based generic views were introduced to abstract these patterns and ease view development for the common cases.

> The problem with function-based generic views is that while they covered the simple cases well, there was no way to extend or customize them beyond some simple configuration options, limiting their usefulness in many real-world applications.

> Class-based generic views were created with the same objective as function-based generic views, to make view development easier. However, the way the solution is implemented, through the use of mixins, provides a toolkit that results in class-based generic views being more extensible and flexible than their function-based counterparts.

> If you have tried function based generic views in the past and found them lacking, you should not think of class-based generic views as simply a class-based equivalent, but rather as a fresh approach to solving the original problems that generic views were meant to solve.

> The toolkit of base classes and mixins that Django uses to build class-based generic views are built for maximum flexibility, and as such have many hooks in the form of default method implementations and attributes that you are unlikely to be concerned with in the simplest use cases. For example, instead of limiting you to a class-based attribute for form_class, the implementation uses a get_form method, which calls a get_form_class method, which in its default implementation just returns the form_class attribute of the class. This gives you several options for specifying what form to use, from a simple attribute, to a fully dynamic, callable hook. These options seem to add hollow complexity for simple situations, but without them, more advanced designs would be limited.

简单说明:
最开始只有视图函数, django传给你Http请求,然后要求你返回Http回应,这就是django为什么要扩展视图原因.

视图函数处理简单情况可以,但是无法扩展和订制,这就会限制在真正web应用上.

视图类通过设计模式,最大化其能力.

视图类是提供一个mixins,最少的工具,从而更容易扩展.

视图工具类和混合使django能够建立视图和最大化其扩展性,比如有许多回调和属性可以重写,这也许会让你认为其过于复杂.


![](http://7xnnj6.com1.z0.glb.clouddn.com/django-view-class.jpg)
