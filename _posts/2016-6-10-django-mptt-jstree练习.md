---
layout: post
title: django-mptt视图使用jstree
category: 学习
keywords: 学习,2016
---

练习目的
掌握jstree和django-mptt的使用

![](http://7xnnj6.com1.z0.glb.clouddn.com/djangodjango-mptt-jstree.png)


关健代码

```

def genre_jstree(root, data=dict):
    if hasattr(data, '__call__'):
        data = data()
    data['text'] = root.name
    children = root.children.all()
    if len(children) > 0:
        data['children'] = []
        for n in children:
            data['children'].append(genre_jstree(n))
    return data


def genre_jstree_v(request):
    root = Genre.objects.first().get_root()
    return JsonResponse(genre_jstree(root))


```
![](http://7xnnj6.com1.z0.glb.clouddn.com/djangodjango-mptt-tree-html.png)


## 参考
[](https://github.com/vakata/jstree#populating-the-tree-using-ajax)
