#!/usr/bin/python3
"""
This module contains the definition of text_indentation()
"""


def text_indentation(text):
    """Prints 2 new lines after each of these characters: ., ? and :
    Args:
            text (str): the text to be printed.
    Raises:
            TypeError: if text is not a string.
    """
    if not type(text) is str:
        raise TypeError("text must be a string")

    index = 0
    while index < len(text):
        if text[index] == "." or text[index] == "?" or text[index] == ":":
            print(text[index], end="")
            print("\n\n", end="")
            index += 1
            while index < len(text):
                if text[index] != " ":
                    break
                index += 1
        if index < len(text):
            print(text[index], end="")
        index += 1
