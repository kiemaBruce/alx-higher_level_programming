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
                x (int): horizontal offset when printing a Rectangle object.
                y (int): vertical offset when printing a Rectangle object.
                id: identifies the Rectangle object.
        """
        super().__init__(id)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("x", x)
        self.integer_validator("y", y)

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
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Returns the height of the Rectangle object."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the self.__height attribute."""
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Returns the self.__x attribute of the Rectangle object."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the self.__x attribute."""
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Returns the self.__y attribute of the Rectangle object."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the self.__y attribute."""
        self.integer_validator("y", value)
        self.__y = value

    def integer_validator(self, name, value):
        """Validates the width, height, x and y attributes."""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError(f"{name} must be > 0")
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints out the Rectangle instance to stdout using '#'."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width):
                if j == 0:
                    for b in range(self.__x):
                        print(" ", end="")
                print("#", end="")
                if j == self.__width - 1:
                    print()

    def __str__(self):
        """Returns a user-readable string representation of a Rectangle object.
        """
        class_name = self.__class__.__name__
        ret_s = (
            f"[{class_name}] "
            + f"({self.id}) {self.__x}/{self.__y} - "
            + f"{self.__width}/{self.__height}"
        )
        return ret_s

    def update(self, *args, **kwargs):
        """ Updates Rectangle attributes.
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            if kwargs:
                for key in kwargs:
                    if key == "id":
                        self.id = kwargs[key]
                    if key == "width":
                        self.width = kwargs[key]
                    if key == "height":
                        self.height = kwargs[key]
                    if key == "x":
                        self.x = kwargs[key]
                    if key == "y":
                        self.y = kwargs[key]
