#!/usr/bin/env python3

# import asyncio

# async_generator = __import__('0-async_generator').async_generator



import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    return await(measure_runtime())

print(
    asyncio.run(main())
)
