#!/usr/bin/env python3

"""
    Defines a regular function that takes an integer
    and return an asyncio.Task
"""

# from typing import Any
import asyncio

try:
    wait_random = __import__('0-basic_async_syntax').wait_random
except ImportError:
    pass


def task_wait_random(max_delay):
    """
     Creates and returns an asyncio.Task for the
     wait_random coroutine with the given max_delay.

    :param max_delay: (int) maximum delay in seconds for
                      the wait coroutine.
    :return: An asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
