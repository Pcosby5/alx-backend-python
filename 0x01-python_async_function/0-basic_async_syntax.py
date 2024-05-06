#!/usr/bin/env python3

import random
import asyncio


async def wait(delay_max: float = 10) -> float:
    """Wait for a random time between 0 and delay_max seconds.

    Args:
        delay_max (float): The maximum delay in seconds.
            Defaults to 10 seconds.

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, delay_max)
    await asyncio.sleep(delay)
    return delay
