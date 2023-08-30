#!/usr/bin/python3
""" This module contains a Square class definition
"""


class Square:
    """This class defines a square object"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ Initializes fields

        Args:
                _size: the size of the square
        """
        self.size(size)
        self.position(position)

    def area(self):
        """Returns the current square area

        Returns:
            the square of self.size
        """
        if type(self.__size) is int:
            if self.__size < 0:
                raise ValueError("size must be >= 0")
            else:
                area = self.__size * self.__size
                return area
        else:
            raise TypeError("size must be an integer")

    def size(self):
        """getter for the size attribute"""
        return self.__size

    def size(self, value):
        """setter for self.size attribute
        Args:
            value: To replace the current value of the self.size attribute
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Prints out the square to stdout using #"""
        pos_string = self.__position[0] * " "
        if self.size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print(pos_string, end="")
                for i in range(0, self.__size):
                    print("#", end="\n" if i == self.__size - 1 else "")

    def position(self):
        """getter for self.position attribute"""
        return self.__position

    def position(self, value):
        """setter for self.position attribute
        Args:
            value: to replace the current value of the self.position attribute
        """
        te_s = "position must be a tuple of 2 positive integers"
        if isinstance(value, tuple):
            for i in value:
                if isinstance(i, int):
                    if i >= 0:
                        self.__position = value
                    else:
                        raise TypeError(
                            "position must be a tuple of 2 positive integers"
                        )
                else:
                    raise TypeError(te_s)
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
