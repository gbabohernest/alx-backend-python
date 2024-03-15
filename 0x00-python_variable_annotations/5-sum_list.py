#!/usr/bin/env python3

"""
    Defines a type-annotated function that takes a list
    of floats as argument and return their sum as float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A type-annotated function that return the
    sum of float values as a float

    :param input_list: A list of float values
    :return:  The sum of all the values as float value
    """
    answer: float = 0
    for i in input_list:
        answer = answer + i
    return answer
