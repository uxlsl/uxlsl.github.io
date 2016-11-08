# -*- coding:utf-8 -*-
"""

async 的函数调用后返回coroutine对象
even_loop.run_until_complete 参数要functure

"""
import asyncio


async def hello():
    return "hello"


loop = asyncio.get_event_loop()
try:
    result = loop.run_until_complete(hello())
    print(result)
except:
    pass