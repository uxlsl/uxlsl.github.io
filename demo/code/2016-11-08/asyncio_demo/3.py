
import asyncio


async def foo():
    print("foo sleep")
    await asyncio.sleep(3)
    print("foo up")


async def bar():
    print("bar sleep")
    await asyncio.sleep(3)
    print("bar up")


loop = asyncio.get_event_loop()
try:
    loop.call_soon(foo)
    loop.call_soon(bar)
    loop.run_forever()
finally:
    print("end loop")
