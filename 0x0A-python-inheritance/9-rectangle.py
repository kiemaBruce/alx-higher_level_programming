#!/usr/bin/python3
"""
This module defines the BaseGeomery and Rectangle class.
"""


class BaseGeometry:
    """Definition of the BaseGeometry class."""

    def area(self):
        """Raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Args:
                value (int): the value that is to be validated.
                name (str): identifier of the value.
        Raises:
                TypeError: if value is not an integer.
                ValueError: if value is not greater than 0 or if name is not a
                string.
        """
        if not type(value) is int:
            raise TypeError(f"{name:s} must be an integer")
        if value <= 0:
            raise ValueError(f"{name:s} must be greater than 0")


class Rectangle(BaseGeometry):
    """Definition of the Rectangle class."""

    def __init__(self, width, height):
        """Initializes class attributes.
        Args:
                width (int): width of the Rectangle.
                height (int): height of the Rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a user-readable string representation of the Rectangle object."""
        return "[Rectangle] " + f"{self.__width}/{self.__height}"
