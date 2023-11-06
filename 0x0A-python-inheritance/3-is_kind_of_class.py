#!/usr/bin/python3
"""Defines the is_kind_of_class() method.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance directly or indirectly.
    Args:
            obj: the object to be checked.
            a_class: the class against which 'obj' is to be checked.
    Returns:
            bool: True if the object is an instance of, or if the object is
            an instance of a class that inherited from a_class. False
            otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
