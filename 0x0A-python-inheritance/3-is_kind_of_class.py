#!/usr/bin/python3
"""
This module contains the definition of the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """Determines whether an object is an instance of a class.
    Args:
            obj: the object to be analyzed.
            a_class: the class against which obj is to be checked.
    Return: True if if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class ;
    otherwise False.
    """
    return isinstance(obj, a_class)
