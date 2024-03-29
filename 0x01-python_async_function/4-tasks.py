#!/usr/bin/env python3
"""
    Generates a list of asyncio.Tasks for
    random delays using task_wait random()
"""

import asyncio
from typing import List, Any

try:
    task_wait_random = __import__('3-tasks').task_wait_random
except ImportError:
    pass


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Generate a list of asyncio.Tasks for random
    delays using task_wait_random.

    :param n: (int) The number of random delays to generate.
    :param max_delay: (int) The maximum delay in seconds.
    :return: A list of asyncio.Tasks
    """
    tasks = []
    for _ in range(n):
        task = await task_wait_random(max_delay)
        tasks.append(task)
    return sorted(tasks)
