---
layout: post
title:
category: 学习
keywords: 学习,2016
---


## asyncio 重温

环境：
python3.5


## asyncio 作用
异步io提速, 在处理多个io的时候相当有用!


## asyncio 的一些关键字

async, await

由async 标示的方法由await来等待


## asyncio 的一些常用方法

loop = asyncio.get_event_loop

loop.run_until_done

loop.run_forever

asyncio.await **重点** 实现同时等待多个协程的方法，也就是可以等待多个io


## 多个请求的例子

```

import asyncio
import aiohttp

async def phase(i):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/ip') as resp:
            result = await resp.json()
            return result

async def main(num_phases):
    print('starting main')
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print('waiting for phases to complete')
    completed, pending = await asyncio.wait(phases)
    results = [t.result() for t in completed]
    print('results: {!r}'.format(results))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(100))
finally:
    event_loop.close()


```
