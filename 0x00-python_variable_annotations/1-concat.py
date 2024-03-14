#!/usr/bin/env python3

"""Basic annotation - concat"""


def concat(str1: str, str2: str) -> str:
    """
    A type annotated function concat that
    takes two string values as argument and
    return a concatenated string
    :param str1: str value.
    :param str2: str value.
    :return: A concatenated str
    """
    return "{}{}".format(str1, str2)
