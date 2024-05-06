#!/usr/bin/env python3
"""Wait for a random time between 0 and delay_max seconds.
"""

import random
import asyncio


async def wait(delay_max: float = 10.0) -> float:
    """Wait for a random time between 0 and delay_max seconds.

    Args:
        delay_max (float): The maximum delay in seconds.
            Defaults to 10 seconds.

    Returns:
        float: The actual delay in seconds.
    """
    delay: float = random.uniform(0.0, delay_max)
    await asyncio.sleep(delay)
    return delay
