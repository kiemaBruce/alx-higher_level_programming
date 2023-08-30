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
        self.size(size)

    def area(self):
        """Returns the current square area

        Returns:
            the square of self.size
        """
        if type(self.size) is int:
            if self.size < 0:
                raise ValueError("size must be >= 0")
            else:
                area = self.size * self.size
                return area
        else:
            raise TypeError("size must be an integer")

    def size(self):
        """getter for the __size attribute"""
        return self._size

    def size(self, value):
        """setter for self.__size attribute
        Args:
            value: To replace the current value of the self.__size attribute
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Prints out the square to stdout using #"""
        if self.size == 0:
            print()
        else:
            for i in range(0, self.size):
                for i in range(0, self.size):
                    print("#", end="\n" if i == self.size - 1 else "")
