#!/usr/bin/python3

"""
Definition of the write_file function.
"""


def write_file(filename="", text=""):
    """Writes a string to a file overwriting old contents.
    Args:
            filename (str): the name of the file.
            text (str): the string to be written to the file.
    Returns:
            int: the number of characters written .
    """
    with open(filename, "w", encoding="utf-8") as myfile:
        r = myfile.write(text)
    return r
