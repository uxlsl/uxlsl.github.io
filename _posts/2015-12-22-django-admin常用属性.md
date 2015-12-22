---
layout: post
title: django-admin常用操作笔记
category: 学习
keywords: 学习,2015
---
对于模型
属性
1. 搜索 search_fields
2. 过滤 list_filter
3. 显示 list_display
4. 添加 fields
5. 排序 ordering

动作
actions


*基本上都为列表形式*

加入管理
admin.site.register

# 总结
如果对显示不关心,基本上上面五个属性加动作已经够用了

# 例子

demo/code/2015-12-22/myadmin

``` admin.py

from django.contrib import admin
from .models import SuperHero

class SuperHeroAdmin(admin.ModelAdmin):
    list_display = ("name", 'added_on')
    search_fields = ["name"]
    ordering = ["name"]
    list_filter = ("name", "added_on")
    actions = ['foo_and_bar']
    def foo_and_bar(self, request, queryset):
        queryset.update(name="foo_and_bar")

admin.site.register(SuperHero, SuperHeroAdmin)

```
