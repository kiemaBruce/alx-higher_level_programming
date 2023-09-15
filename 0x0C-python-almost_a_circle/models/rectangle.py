#!/usr/bin/python3
"""
This module defines the Rectangle class.
"""


from .base import Base


class Rectangle(Base):
    """Definition of the Rectangle class attributes."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle object.
        Args:
                width (int): width of the Rectangle.
                height (int): height of the Rectangle.
                x: extra argument.
                y: second extra argument.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width of the Rectangle object."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the self.__width attribute."""
        self.__width = value

    @property
    def height(self):
        """Returns the height of the Rectangle object."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the self.__height attribute."""
        self.__height = value

    @property
    def x(self):
        """Returns the self.__x attribute of the Rectangle object."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the self.__x attribute."""
        self.__x = value

    @property
    def y(self):
        """Returns the self.__y attribute of the Rectangle object."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the self.__y attribute."""
        self.__y = value
