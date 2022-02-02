#!/usr/bin/env python3
"""async routine called wait_n that
takes in 2 int arguments (in this order):
n and max_delay. You will spawn wait_random n
times with the specified max_delay."""
import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """return the list of all the delays (float values)."""
    results: typing.List[float] = []
    for delay in range(n):
        results.append(asyncio.create_task(wait_random(max_delay)))
    return await asyncio.gather(*results)
