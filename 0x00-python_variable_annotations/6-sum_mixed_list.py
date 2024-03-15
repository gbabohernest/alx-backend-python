#!/usr/bin/env python3

"""Defines a complex types annotation - mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A type-annotated function that takes a list of
    mixed types(int, float) and return the sum of
    all values as a float.

    :param mxd_lst: A List that will contain both int and float values.
    :return: The sum of all values as a float
    """

    ans: float = 0

    for i in mxd_lst:
        ans = ans + i

    return ans
