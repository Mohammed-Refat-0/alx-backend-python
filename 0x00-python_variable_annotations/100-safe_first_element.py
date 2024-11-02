#!/usr/bin/env python3
"""safe_first_element module"""

import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Duck-typed annotated function"""
    if lst:
        return lst[0]
    else:
        return None
