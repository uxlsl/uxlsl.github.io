
import asyncio

async def f1():
    print("f1")
    return "f1"

async def f2():
    result = await f1()
    print(result)
    return "f2"

loop = asyncio.get_event_loop()
try:
    result = loop.run_until_complete(f2())
    print(result)
finally:
    print("exit")
