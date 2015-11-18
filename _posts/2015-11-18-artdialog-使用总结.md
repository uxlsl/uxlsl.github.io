---
layout: post
title: artDialog 使用总结
category: 学习
keywords: 学习,2015
---

# artDialog 使用总结

## content
dialog
content **重要** String, HTMLElement
HTMLElement document.getElementById("XXX")
因为可以使用HTMElement,因此有时要隐藏
style="visibility:visible;"
style="visibility:hidden;"
style="display:none;"
style="display:block;"

jquery
$("XXX").hide()
$("XXX").show()

**注意**
1. 在conent中使用 document.getElementById默认会从文档中消失,就是吃掉了, 因此不建设使用,为什么会这样,我还在查.
使用备用方案, $("xxx").clone()
2. 按扭何时出现,当使用ok 函数不为空时,就会出现.返回true,则是关闭.

# 意外收获

setTimeout
