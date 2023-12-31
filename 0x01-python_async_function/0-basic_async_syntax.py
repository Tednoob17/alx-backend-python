#!/usr/bin/env python3
"""
Basic Async Syntax
"""


async def wait_random(max_delay: int = 10) -> float:
    """Wait random from 0 to max_delay"""
    rand: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
