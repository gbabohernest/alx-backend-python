#!/usr/bin/env python3

"""Defines complex types annotation - string and int/float to tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """
    A type-annotated function that returns a tuple

    :param k: str value
    :param v: Union of int or float
    :return: A tuple the arguments values
    """
    sqrt: float = v * v
    ans = (k, sqrt)
    return ans
