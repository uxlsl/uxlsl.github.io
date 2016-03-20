---
layout: post
title:  flask raise Exception 笔记
category: 学习
keywords: 学习,2016
---

这倒是人尽其才，物尽其用，两全其美。  -- 马烽《典型事例》


## flask 实现 api 的好处

1. 对指定的异常能单独处理
2. 能够控制异常的输出


```
# 1
@app.route('/foo')
def get_foo():
    raise InvalidUsage('This view is gone', status_code=410)

# 2
@app.errorhandler(InvalidAPIUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# 3
from flask import jsonify

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv



```






## 参考

[Implementing API Exceptions](http://flask.pocoo.org/docs/0.10/patterns/apierrors/)
