#!/usr/bin/python3
"""Defines the Rectangle class.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of Rectangle class."""

    def __init__(self, width, height):
        """Initializes instance attributes.
        Args:
                width (int): the width of the Rectangle.
                height (int): the height of the Rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
