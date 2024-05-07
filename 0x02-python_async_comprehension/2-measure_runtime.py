#!/usr/bin/env python3
"""Measures the total runtime of executing
    async_comprehension four times in parallel.
"""

import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: The total runtime in seconds.
    """

    # Get the current event loop's time
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        *[async_comprehension() for _ in range(4)]  # noqa: E231
    )

    # Get the current event loop's time again after completion
    end_time = asyncio.get_event_loop().time()

    # Return the total runtime
    return end_time - start_time
