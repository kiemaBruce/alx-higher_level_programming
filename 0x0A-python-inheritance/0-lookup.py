#!/usr/bin/python3
"""
This module contains the lookup function
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object:
    Args:
            obj: the object whose attributes and methods are to be returned.
    """
    return dir(obj)
