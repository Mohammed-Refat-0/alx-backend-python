#!/usr/bin/env python3
"""async_generator module"""

from typing import AsyncIterator
from random import uniform
from asyncio import sleep


async def async_generator() -> AsyncIterator[float]:
    """loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for i in range(10):
        await sleep(1)
        yield uniform(0, 10)
