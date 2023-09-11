#!/usr/bin/python3
"""
This module defines the inherits_from function.
"""


def inherits_from(obj, a_class):
    """Determines whether an object inherites from a subclass.
    Args:
            obj: the object that is to be checked.
            a_class: the class against which obj is to be checked.
    Return:
            bool: True if the object is an instance of a class that
            inherited (directly or indirectly) from the specified
            class ; otherwise False.
    """
    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
