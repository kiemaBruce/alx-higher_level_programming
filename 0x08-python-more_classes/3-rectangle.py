#!/usr/bin/python3
"""
This module contains the definition of the Rectangle class.
"""


class Rectangle:
    """
    Defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """initializes the width and height
        Args:
                width (int): Width of the rectangle
                height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the self.__width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the self.__width

        Checks whether the value of the width is an int and whether it
        is greater than or equal to 0 before setting it.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the self.__height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the self.__height

        Checks whether the value of the height is an int and wheter it
        is greater than or equal to zero before setting it.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle area"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle using '#'"""
        ret_s = ""
        for i in range(self.__height):
            for j in range(self.__width):
                ret_s += "#"
            if i != (self.__height - 1):
                ret_s += "\n"
        return ret_s
