#!/usr/bin/env python3


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> "AsyncGenerator[float, None]":
    """
    An async generator that generates 10 random numbers between 0 and 10,
    one per second.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        # Generate and yield a random number between 0 and 10
        yield random.uniform(0, 10)
