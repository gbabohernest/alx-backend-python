#!/usr/bin/env python3

"""Defines asynchronous coroutines for generating random delays."""

from typing import List

try:
    wait_random = __import__('0-basic_async_syntax').wait_random
except ImportError:
    pass


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Generate a list of random delays.

    :param n:(int) The number of random delays to generate.
    :param max_delay:(int) The maximum delay in seconds.
    :return: List[float]: A list of random delays as floats.
    """
    all_delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        all_delays.append(delay)
    return sorted(all_delays)
