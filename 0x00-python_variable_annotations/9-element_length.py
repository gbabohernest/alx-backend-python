#!/usr/bin/env python3

"""Defines a way to Duck type an iterable object"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A function that duck type an iterable object.

    :param lst: Iterable
    :return: List
    """
    return [(i, len(i)) for i in lst]
