#!/usr/bin/env python3
""" element_length module
    """
from typing import Iterable


def element_length(lst: Iterable):
    return [(i, len(i)) for i in lst]
