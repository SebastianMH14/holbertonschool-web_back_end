#!/usr/bin/env python3
""" coroutine called async_generator that takes no arguments.
The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10."""
import asyncio
import random
import typing


async def async_generator():
    """loop 10 times, each time
    asynchronouslywait 1 second,
    then yield a random number
    between 0 and 10."""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
