#!/usr/bin/python3
"""
This module contains the add_integer function.
>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """ adds two integers and returns the result
        Args:
            a: first integer.
            b: second integer; default value is 98.
        Returns:
            int: the arithmetic sum of a and b. The result is cast to an
            integer.
        Raises:
            TypeError: if either a or b is not an integer or float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
