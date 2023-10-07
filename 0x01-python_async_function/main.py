#!/usr/bin/env python3

# import asyncio

# wait_random = __import__('0-basic_async_syntax').wait_random

# print(asyncio.run(wait_random()))
# print(asyncio.run(wait_random(5)))
# print(asyncio.run(wait_random(15)))

# import asyncio

# wait_n = __import__('1-concurrent_coroutines').wait_n

# print(asyncio.run(wait_n(5, 5)))
# print(asyncio.run(wait_n(10, 7)))
# print(asyncio.run(wait_n(10, 0)))

# measure_time = __import__('2-measure_runtime').measure_time

# n = 5
# max_delay = 9

# print(measure_time(n, max_delay))

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
