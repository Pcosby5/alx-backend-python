#!/usr/bin/env python3
"""
    Collects 10 random numbers from the
    async_generator() using async comprehension.
"""

from typing import List
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from the
    async_generator() using async comprehension.

    Returns:
        List[float]: list of 10 random numbers
    """
    # Using async comprehension to collect 10 random numbers
    # from the async_generator()
    return [
        i
        async for i in async_generator()
    ]
