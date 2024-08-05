#!/usr/bin/env python3
'''
    task_wait_n module
'''
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the random generated delays (n times),
    using asyncio.gather
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_list = await asyncio.gather(*tasks)
    return sorted(completed_list)
