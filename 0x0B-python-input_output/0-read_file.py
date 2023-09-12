#!/usr/bin/python3

"""
This module contains the definition of the read_file function.
"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout.
    Args:
            filename (str): the name of the file to be opened and read from.
    """
    with open(filename, "r", encoding="utf-8") as myfile:
        text = myfile.read()
        print(text, end="")
