#!/usr/bin/python3
"""Defines the print_sorted() method.
"""


class MyList(list):
    """Specifies custom behaviour for the list class."""

    def print_sorted(self):
        """Prints a list of ints sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
