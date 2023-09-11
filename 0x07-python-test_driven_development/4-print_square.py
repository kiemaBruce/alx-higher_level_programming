#!/usr/bin/python3
"""
This module defines the print_square method
"""


def print_square(size):
    """Prints a square using the '#' character
    Args:
            size (int): The size of the square
    Raises:
            TypeError: if size is not an integer or if size is a float and
                        is less than zero.
            ValueError: if size is less than 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
