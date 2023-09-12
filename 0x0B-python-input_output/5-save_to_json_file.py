#!/usr/bin/python3
"""
This module contains the definition of the save_to_json_file function.
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation
    Args:
            my_obj: the object to be written into a file in JSON format.
            filename: the name of the file into which my_obj is to be
            written.
    """
    with open(filename, "w", encoding="utf-8") as myfile:
        json.dump(my_obj, myfile)
