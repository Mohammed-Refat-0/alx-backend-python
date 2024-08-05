#!/usr/bin/env python3
"""wait_random module"""

from random import uniform
from asyncio import sleep


async def wait_random(max_delay=10):
    """wait a random amount between 0 and 10 seconds"""
    await sleep(uniform(0, max_delay))
