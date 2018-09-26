---
layout: post
title: django app config
category: 学习
keywords: 学习,2018
---

# django app config 

使用原因:

However, there’s a few places where Django needs to interact with installed applications, mainly for configuration and also for introspection. That’s why the application registry maintains metadata in an AppConfig instance for each installed application.

解释:
django要与安装的app进行交互,如属性,配置,model等等,进行信号绑定

个人感想:
app配置可以独立与settings,更加方便地用到其他项目上


## 使用

```

>>> from django.apps import apps
>>> apps.get_app_config('admin').verbose_name
'Admin'


```


## 参考

1. https://docs.djangoproject.com/en/2.1/ref/applications/
