#!/usr/bin/python3
"""Defines the Square class.
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class attributes and methods."""

    def __init__(self, size):
        """Initializes instance attributes.
        Args:
                size (int): dimensions of one side of the square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the Square object."""
        return self.__size * self.__size
