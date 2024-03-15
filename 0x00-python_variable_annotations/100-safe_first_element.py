#!/usr/bin/env python3

"""Defines the correct duck-typed annotations"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Augment the correct duck-typed annotations

    :param lst: List of any value(s)
    :return:  Any or None
    """
    if lst:
        return lst[0]
    else:
        return None
