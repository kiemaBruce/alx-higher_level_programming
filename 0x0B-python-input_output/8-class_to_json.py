#!/usr/bin/python3
"""
This module contains the definition of the class_to_json function.
"""


def class_to_json(obj):
    """Returns dictionary description of a class object
    Args:
            obj: the class object.
    Returns:
            dict: Dictionary description of a class object.
    """
    return obj.__dict__
