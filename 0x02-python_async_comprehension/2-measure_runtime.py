#!/usr/bin/env python3
"""measure_runtime module"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure toltal time to execute async_comprehension 4 times"""
    start_time = time.time()
    list_of_delays = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*list_of_delays)
    return time.time() - start_time
