#!/usr/bin/env python3
"""
Safety get value
"""
from typing import Any, Mapping, TypeVar, Optional, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
