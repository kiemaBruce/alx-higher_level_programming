#!/usr/bin/python3
"""Contains definition of Rectangle class.
"""


import models.base as base


class Rectangle(base.Base):
    """Rectangle class which inherits from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance attributes.
        Args:
                width (int): the width of the Rectangle object.
                height (int): the height of the Rectangle object.
                x (int): extra argument.
                y (int): extra argument.
                id (int): the id of the Rectangle object.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the value of the width of the Rectangle object."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Returns the value of the height of the Rectangle object."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Returns the value of the x of the Rectangle object."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Returns the value of the y of the Rectangle object."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
