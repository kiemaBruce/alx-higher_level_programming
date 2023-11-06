#!/usr/biin/python3
"""Contains definition of MyInt class that inherits from int.
"""


class MyInt(int):
    """Attributes and methods of MyInt class."""

    def __eq__(self, value):
        """Inverts the equal comparison operator for ints.
        Returns:
                bool: True if self is not equal to value, and False if
        self is equal to value.
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """Inverts not equal to comparison operator for ints.
        Returns:
                bool: True if self is equal to value, and False if self
                is not equal to value.
        """
        return super().__eq__(value)
