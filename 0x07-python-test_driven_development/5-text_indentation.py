#!/usr/bin/python3

"""
This module defines the text_indentation function.
"""


def text_indentation(text):
    """Prints a string replacing '.', '?' and ':' with double newline
    Args:
            text (str): the string that is to be printed.
    Raises:
            TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 9
    for index, char in enumerate(text):
        if c == -1 and char == " ":
            continue
        if char == "." or char == "?" or char == ":":
            print("\n")
            c = -1
            continue
        print(char, end="")
        c = 9
