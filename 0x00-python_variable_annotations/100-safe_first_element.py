#!/usr/bin/env python3
"""
Duck Typing - first element of a sequence
"""
from typing import Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Any | None:
    if lst:
        return lst[0]
    else:
        return None
