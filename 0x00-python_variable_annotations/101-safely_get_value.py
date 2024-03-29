#!/usr/bin/env python3

"""More involved type annotation"""

from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')  # Value Type


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """
    Add type annotation to the function
    :param dct:
    :param key:
    :param default:
    :return:
    """
    if key in dct:
        return dct[key]
    else:
        return default
