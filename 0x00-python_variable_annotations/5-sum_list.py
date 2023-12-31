#!/usr/bin/env python3
"""
Type-annotated sum_list function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum of input_list"""
    return float(sum(input_list))
