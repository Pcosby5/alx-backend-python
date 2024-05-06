#!/usr/bin/env python3
'''
    The basics of async.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random time between 0 and max_delay (included and float value)
    seconds and eventually returns it.

    Args:
        max_delay (int): The maximum delay in seconds.
            Defaults to 10 seconds.

    Returns:
        float: The actual delay in seconds.
    """
    # Generate a random delay between 0 and max_delay
    delay: float = random.uniform(0, max_delay)

    # Suspend the execution of the current task for the generated delay
    await asyncio.sleep(delay)

    # Return the generated delay
    return delay
