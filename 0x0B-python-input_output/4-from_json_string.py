#!/usr/bin/python3
"""
This module containst the definition of the from_json_string function.
"""

import json


def from_json_string(my_str):
    return json.loads(my_str)
