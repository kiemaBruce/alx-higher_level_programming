#!/usr/bin/python3
"""
This module contains the definition of the add_integer function.
"""


def add_integer(a, b=98):
    """Adds two integers.
    Args:
            a (int): the first integer.
            b (int): the second integer. It has a default value of 98.
    Returns:
            int: The sum of the two numbers.
    Raises:
            TypeError: If a or b is not an integer.
    """
    if not type(a) is int and not type(a) is float:
        raise TypeError("a must be an integer")
    if not type(b) is int and not type(b) is float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
