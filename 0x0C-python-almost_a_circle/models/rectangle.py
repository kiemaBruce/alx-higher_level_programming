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
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of the height of the Rectangle object."""
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the value of the x of the Rectangle object."""
        return self.__x

    @x.setter
    def x(self, value):
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the value of the y of the Rectangle object."""
        return self.__y

    @y.setter
    def y(self, value):
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance to stdout using '#'"""
        for i in range(self.__y):
            print("\n", end="")
        for i in range(self.__height):
            for j in range(self.__width):
                if j == 0:
                    for k in range(self.__x):
                        print(" ", end="")
                print('#', end="\n" if j == self.__width - 1 else "")

    def __str__(self):
        """Returns human-readable string representation of instance."""
        r_str = (
            "[Rectangle] "
            + f"({self.id}) {self.__x}/{self.__y} "
            + f"- {self.__width}/{self.__height}"
        )
        return r_str

    def update(self, *args, **kwargs):
        """Updates Rectangle attributes."""
        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if index == 1:
                    self.width = value
                if index == 2:
                    self.height = value
                if index == 3:
                    self.x = value
                if index == 4:
                    self.y = value
        elif kwargs:
            for key in kwargs:
                setattr(self, key, kwargs[key])
