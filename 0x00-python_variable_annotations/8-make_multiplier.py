#!/usr/bin/env python3
"""
Multiply a float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return function that multiplies a float by multiplier"""
    return lambda x: x * multiplier
