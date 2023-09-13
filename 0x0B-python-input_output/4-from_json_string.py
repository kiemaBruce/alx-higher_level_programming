#!/usr/bin/python3
"""
This module containst the definition of the from_json_string function.
"""

import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string.
    Args:
         my_str (str): the JSON string.
    Returns:
        Python Object: the equivalent Python object of a JSON string.
    """
    return json.loads(my_str)
