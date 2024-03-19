#!/usr/bin/env python3

"""Defines an async generator that yields random numbers 0 - 10."""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """
    Defines an asynchronous generator that generates
    / yields random number between 0 and 10
    :return: A Generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
