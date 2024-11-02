#!/usr/bin/env python3
"""safe_get_value module"""

from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Def = Union[T, None]
Result = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Result:
    '''Retrieves a value from a dict for a given key'''
    if key in dct:
        return dct[key]
    else:
        return default
