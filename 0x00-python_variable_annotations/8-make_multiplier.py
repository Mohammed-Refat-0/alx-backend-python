#!/usr/bin/env python3

""" make_multiplier function module"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    '''Creates a multiplier function
    '''
    return lambda x: x * multiplier
