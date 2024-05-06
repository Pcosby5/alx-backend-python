#!/usr/bin/env python3
"""Asynchronous function that
spawns wait_random n times with the specified max_delay.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that spawns wait_random n times with the specified
    max_delay.

    Args:
        n (int): The number of times to spawn wait_random coroutine.
        max_delay (int): The maximum delay for each random wait time.

    Returns:
        List[float]: list of all the delays (float values) in ascending order.
    """
    # Create a list to store the tasks
    tasks = []

    # Spawn wait_random n times with the specified max_delay
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    # Wait for all tasks to complete concurrently
    completed_tasks = await asyncio.gather(*tasks)

    # Return the list of delays sorted in ascending order
    return sorted(completed_tasks)
