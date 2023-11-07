#!/usr/bin/python3
"""Contains definition of append_write() function.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file(UTF8)
    Args:
            filename (str): the file path of the file to into which the
                            string is to be appended.
            text (str): the string to be appended at the end of the file.
    Returns:
            int: the number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as myfile:
        chars = myfile.write(text)
    return chars
