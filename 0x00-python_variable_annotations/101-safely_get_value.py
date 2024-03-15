#!/usr/bin/env python3

"""More involved type annotation"""

from typing import TypeVar, Mapping, Any, Optional

KT = TypeVar('KT')  # Key Type
VT = TypeVar('VT')  # Value Type


def safely_get_value(dct: Mapping, key: Any, default:
                     Optional[VT] = None) -> Optional[VT]:
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
