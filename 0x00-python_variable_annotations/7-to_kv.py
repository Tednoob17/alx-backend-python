#!/usr/bin/env python3
"""
Takes a string k and an int OR float v as arguments and returns a tuple.
"""
from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    """Return tuple of k and v squared"""
    return (k, float(v ** 2))
