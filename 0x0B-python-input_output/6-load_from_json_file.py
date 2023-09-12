#!/usr/bin/python3
"""
This module defines the load_from_json_file function.
"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.
    Args:
            filename (str): the name of the file that contains the JSON
                            string.
    Return: the Python object created from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as myfile:
        py_object = json.load(myfile)
    return py_object
