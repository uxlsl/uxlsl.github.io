

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