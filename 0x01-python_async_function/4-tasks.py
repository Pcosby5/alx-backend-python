#!/usr/bin/env python3
""" The basics of async """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random coroutine.
        max_delay (int): The maximum delay for each random wait time.

    Returns:
        List[float]: list of all the delays (float values) in
        ascending order.
    """
    # Create a list of tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Wait for all tasks to complete concurrently
    completed_tasks = await asyncio.gather(*tasks)

    # Return the list of delays sorted in ascending order
    return sorted(completed_tasks)
