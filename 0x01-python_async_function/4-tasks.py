#!/usr/bin/env python3
'''execute multiple coroutines at the same time with async'''

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' Async function that calls task_wait_random n number of times'''
    delays: List = []
    for i in range(n):
        delay = task_wait_random(max_delay)
        delays.append(delay)
    res_list: List = []
    for task in asyncio.as_completed(delays):
        res: float = await task
        res_list.append(res)
    return res_list
