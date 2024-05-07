#!/usr/bin/env python3
"""
    An async generator that generates 10 random numbers between 0 and 10,
    one per second.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator(
    num_iterations: int = 10,
    sleep_time: float = 1.0,
) -> AsyncGenerator[float, None]:
    """
    An async generator that generates random numbers between 0 and 10,
    one per second.

    Args:
        num_iterations (int): The number of random numbers to generate.
            Defaults to 10.
        sleep_time (float): The amount of time to wait between each
            generated number. Defaults to 1 second.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(num_iterations):
        # Asynchronously wait for the specified time
        await asyncio.sleep(sleep_time)
        # Generate and yield a random number between 0 and 10
        yield random.uniform(0, 10)
