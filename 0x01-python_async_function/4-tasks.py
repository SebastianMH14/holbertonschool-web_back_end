#!/usr/bin/env python3
"""ask_wait_n. The code is nearly
identical to wait_n except task_wait_random
is being called."""
import asyncio
import typing

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """return the list of all the delays (float values)."""
    results: typing.List[float] = []
    for delay in range(n):
       results.append(await asyncio.gather(wait_random(max_delay)))
    # response = await asyncio.gather(*results)
    return sorted(results)
