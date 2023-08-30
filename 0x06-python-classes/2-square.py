#!/usr/bin/python3
""" This module contains a Square class definition
"""


class Square:
    """This class defines a square object"""

    def __init__(self, size=0):
        """__init__ Initializes fields

        Args:
                _size: the size of the square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
