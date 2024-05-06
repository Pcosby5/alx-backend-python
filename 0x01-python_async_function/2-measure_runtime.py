#!/usr/bin/env python3
"""Module to measure the runtime of wait_n function."""

import time
from typing import List
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay)
    and return average time per iteration."""

    start_time: float = time.time()  # Record start time

    completed_tasks: List[float] = asyncio.run(wait_n(n, max_delay))  # Execute wait_n

    end_time: float = time.time()  # Record end time

    total_time: float = end_time - start_time  # Calculate total time

    return total_time / len(completed_tasks)  # Return average time per iteration
