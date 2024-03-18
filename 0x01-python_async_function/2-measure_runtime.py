#!usr/bin/env python3

"""Measures the runtime of the wait_n coroutine"""

import asyncio
import time

try:
    wait_n = __import__('1-concurrent_coroutines').wait_n
except ImportError:
    pass


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) &
    return average time per iteration.

    :param n: (int) The number of iterations.
    :param max_delay: (int) The maximum delay in seconds
    :return: The average time per iteration
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
