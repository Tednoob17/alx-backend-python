#!/usr/bin/env python3
"""
Measure the runtime
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime
    """

