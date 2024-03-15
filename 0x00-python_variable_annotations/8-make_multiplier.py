#!/usr/bin/env python3

"""Defines complex types annotation - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
     A type-annotated function that returns a function
     that multiplies a float by multiplier.

     :param multiplier: The multiplier to be used in the returned function
     :return: A function that multiplies a float by multiplier
     """

    def multiplier_function(x: float) -> float:
        """
        Inner function that performs multiplication.

        :param x: The number to be multiplied
        :return: The result of the multiplication
        """
        return x * multiplier

    return multiplier_function
