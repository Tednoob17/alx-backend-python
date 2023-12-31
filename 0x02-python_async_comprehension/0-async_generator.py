#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async Generator that yields random numbers between 0 and 10
    """

