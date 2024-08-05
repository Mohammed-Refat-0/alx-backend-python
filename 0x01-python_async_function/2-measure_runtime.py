# !/usr/bin/env python3
'''
    measure_time module
'''

from typing import List
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> List[float]:
    """
    measures the total execution time for wait_n(n, max_delay)
    returns total_time / n
    """
    start_time = time.time()
    completed_list = await wait_n(n, max_delay)
    elapsed_time = time.time() - start_time
    return (elapsed_time/n)
