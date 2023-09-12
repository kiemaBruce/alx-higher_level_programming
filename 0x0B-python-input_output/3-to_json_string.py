#!/usr/bin/python3
"""
This module contains the definition of the to_json_string funciton.
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.
    Args:
            my_obj: the object whose JSON representation is to be returned.
    Return:
            str: the JSON representation of the object.
    """
    objJSON = json.dumps(my_obj)
    return objJSON
