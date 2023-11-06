#!/usr/bin/python3
"""Defines the is_same_class() method.
"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a class.
    Args:
            obj: the object to be checked.
            class: the class against which obj is to be checked.
    Return: True if obj is exactly an instance of class, and false
            otherwise.
    """
    if isinstance(obj, a_class):
        if (
            issubclass(obj.__class__, a_class)
            and obj.__class__.__name__ != a_class.__name__
        ):
            return False
        return True
    else:
        return False
