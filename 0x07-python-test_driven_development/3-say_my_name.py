#!/usr/bin/python3
"""
This module contains the definition of the say_my_name() function.
"""


def say_my_name(first_name, last_name=""):
    """Prints out the full name.
    Args:
            first_name (str): the first name.
            last_name (str): the last name.
    Raises:
            TypeError: if either first_name or last_name is not a string.
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
