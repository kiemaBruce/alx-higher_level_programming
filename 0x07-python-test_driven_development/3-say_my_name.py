#!/usr/bin/python3
"""
This module contains the say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """Prints out combined first and last names
    Args:
            first_name (str): The first name
            last_name (str): The last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
