#!/usr/bin/python3
"""
This module contains the definition of append_write function.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a file
    Args:
            filename: the file to be written to.
            text: the string to be written into the file.
    Return:
            int: the number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as myfile:
        r = myfile.write(text)
    return r
