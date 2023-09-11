#!/usr/bin/python3
"""
Contains the definition of MyList class that inherits from the list class.
"""


class MyList(list):
    def print_sorted(self):
        """Prints a list in reverse order."""
        print(sorted(self))
