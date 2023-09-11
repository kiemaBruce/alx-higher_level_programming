#!/usr/bin/python3
"""
This module contains the definition of the is_same_class method.
"""


def is_same_class(obj, a_class):
    """Determines whether an object is exactly an instance of a class

    Args:
            obj: object to be analyzed.
            a_class: the class that is to be used to check obj
    Return:
            bool: True if obj is exactly an instance of a_class and
            False if it isn't.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
