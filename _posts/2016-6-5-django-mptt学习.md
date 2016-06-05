---
layout: post
title: django-mptt学习
category: 学习
keywords: 学习,2016
---

## 什么是mptt?
Modified Preorder Tree Traversal
修改排序在树中旅行
MPTT is a technique for storing hierarchical data in a database. 
MPTT 是一种存储分层数据在数据为的一种技术

## django-mptt

### 总体功能

    Simple registration of models - fields required for tree structure will be added automatically.
    The tree structure is automatically updated when you create or delete model instances, or change an instance's parent.
    Each level of the tree is automatically sorted by a field (or fields) of your choice.
    New model methods are added to each registered model for:
        changing position in the tree
        retrieving ancestors, siblings, descendants
        counting descendants
        other tree-related operations
    A TreeManager manager is added to all registered models. This provides methods to:
        move nodes around a tree, or into a different tree
        insert a node anywhere in a tree
        rebuild the MPTT fields for the tree (useful when you do bulk updates outside of django)
    Form fields for tree models.
    Utility functions for tree models.
    Template tags and filters for rendering trees.
    Admin classes for visualizing and modifying trees in Django's administration interface.

自动管理！

```


from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True,related_name='children', db_index=True)
    class MPTTMeta:
        order_insertion_by = ['name']


rock = Genre.objects.create(name="Rock")
blues = Genre.objects.create(name="Blues")
Genre.objects.create(name="Hard Rock", parent=rock)
Genre.objects.create(name="Pop Rock", parent=rock)

```


## 总结

1. 在数据库中处理树的结构时候可能用到！


## 参考

[](https://github.com/django-mptt/django-mptt)
[](http://django-mptt.github.io/django-mptt/tutorial.html#getting-started)

