#!/usr/bin/python3
"""Contains read_file() function.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.
    Args:
            filename(str): the filepath as a string.
    """
    with open(filename, encoding="utf-8") as myfile:
        text = myfile.read()
    print(text, end="")
