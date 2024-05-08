#!/usr/bin/env python3

""" Async Comprehensions """

from asyncio import sleep
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Async Generator that yields random numbers
    between 0 and 10 after a 1 second
    delay.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        # Wait for 1 second before yielding a random number
        await sleep(1)
        # Generate a random number between 0 and 10
        yield uniform(0, 10)
