#!/usr/bin/env python3
'''
    wait_n module
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the random generated delays (n times)
    """
    delay_list = [wait_random(max_delay) for _ in range(n)]
    completed_list = []
    for coro in asyncio.as_completed(delay_list):
        completed_list.append(await coro)
    return completed_list
