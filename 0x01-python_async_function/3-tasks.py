#!/usr/bin/env python3
""" Async basics """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Creates a task for wait_random coroutine with given max_delay.

    Args:
        max_delay (int): The maximum delay for the random wait time.

    Returns:
        Task: A task object that wraps the wait_random coroutine.
    """
    task = create_task(wait_random(max_delay))
    return task
