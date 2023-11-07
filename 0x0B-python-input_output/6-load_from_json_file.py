#!/usr/bin/python3
"""Contains the definition of the load_from_json_file() function.
"""


import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file"""
    with open(filename, mode="r", encoding="utf-8") as myfile:
        py_object = json.load(myfile)
    return py_object
