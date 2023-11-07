#!/usr/bin/python3
"""Contains the definition of the write_file() function.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8).
    Args:
            filename (str): the file path of the file to be written to. It
                            is created if it doesn't exist and if it does
                            exist its contents are overwritten.
            text (str): the string to be written into filename.
    Returns:
            int: the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as myfile:
        chars = myfile.write(text)
    return chars
