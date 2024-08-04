#!/usr/bin/env python3
"""sum_list function module"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """return float sum of list elements
    args:
    input_list: List
    return: float
    """
    return sum(list(map(float, input_list)))
