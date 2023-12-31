#!/usr/bin/env python3
"""
Element_length function
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterale[Sequence]) -> List[Tuple[Sequence, int]]:
    """Tuple of elem and length of elem"""
    return [(i, len(i)) for i in lst]
