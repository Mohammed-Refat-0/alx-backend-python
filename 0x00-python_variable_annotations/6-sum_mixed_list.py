#!/usr/bin/env python3
"""sum_mixed_list function module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """return float sum of list elements
    args:
    input_list: List
    return: float
    """
    return float(sum(mxd_lst))
