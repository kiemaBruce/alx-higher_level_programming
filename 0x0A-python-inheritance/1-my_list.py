#!/usr/bin/python3
"""
Contains the definition of MyList class that inherits from the list class.
"""


class MyList(list):
    """
    Inherits from 'list' class and creates a new class to print list in reverse
    """
    def print_sorted(self):
        """Prints a list in reverse order."""
        new_list = sorted(self)
        print("[", end="")
        for index, value in enumerate(new_list):
            print(f"{value:d}", end="")
            if index != len(self) - 1:
                print(", ", end="")
        print("]")
