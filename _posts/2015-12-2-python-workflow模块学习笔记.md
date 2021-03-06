---
layout: post
title: python-workflow模块学习
category: 学习
keywords: 学习,2015
---

# python-workflow模块学习
工作流
> Workflow engine is a Finite State Machine with memory. It is used to execute set of methods in a specified order
通常用来执行一系列方法在一上指定的次序.

例子:
[
foo,
bar,
baz
]
执行就是foo,bar,baz

## 技巧通过eng实现跳转
eng.stopProcessing  # stops the current workflow
eng.haltProcessing  # halts the workflow (can be used for nested wf engines)
eng.continueNextToken  # can be called many levels deep, jumps up to next token
eng.jumpTokenForward  # will skip the next object and continue with the next one
eng.jumpTokenBack  # will return back, start processing again
eng.jumpCallForward  # in one loop [call, call...] jumps x steps forward
eng.jumpCallBack  # in one loop [call, call...] jumps x steps forward
eng.breakFromThisLoop  # break from this loop, but do not stop processing



```

import time
from workflow.engine import GenericWorkflowEngine


def foo1(obj, eng):
    print("foo1")
    time.sleep(2)


def foo2(obj, eng):
    print("foo2")
    time.sleep(2)

def foo3(obj, eng):
    print("foo3")
    time.sleep(2)

def foo4(obj, eng):
    print("foo4")
    time.sleep(2)
    eng.jumpTokenBack(-2)

wfe = GenericWorkflowEngine()
workflow = [
    foo1,
    foo2,
    foo3,
    foo4,
]


wfe.setWorkflow(workflow)
wfe.process(["a"])


```

## 总结
纯实现流程比这种好一点,也许使用这个目的就是应付下老板,说我使用新技术了.

## 参考

[workflow官方文档](http://workflow.readthedocs.org/en/latest/)
