#!/usr/bin/env python3
"""
Basic Async Syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait random from 0 to max_delay"""

