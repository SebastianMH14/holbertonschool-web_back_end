#!/usr/bin/env python3
"""Async basics in Python task 1"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delayed float values using wait_random coroutine"""
    tasks = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    return [await t for t in asyncio.as_completed(tasks)]
