#!/usr/bin/python3
"""
Defines the print_square() function.
"""


def print_square(size):
    """Prints a square using hashes.
    Args:
            size (int): the dimensions of the square to be printed.
    Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.
            TypeError: if size is a float and is less than zero.
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="\n" if j == size - 1 else "")
