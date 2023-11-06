#!/usr/bin/python3
"""Defines the inherits_from() method.
"""


def inherits_from(obj, a_class):
    """Checks if an object inherits directly or indirectly from a class.
    Args:
            obj: the object to be checked.
            a_class: the class against which obj is to be checked.
    Returns:
            bool: True if the object is an instance of a class that
            inherited (directly or indirectly) from the specified
            class ; otherwise False.
    """
    if issubclass(obj.__class__, a_class):
        if obj.__class__.__name__ != a_class.__name__:
            return True
    return False
