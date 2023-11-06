#!/usr/bin/python3
"""Defines the BaseGeometry class.
"""


class BaseGeometry:
    """Definition of BaseGeometry attributes and methods."""

    def area(self):
        """Raises an exception.
        Raises:
            Exception: always.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.
        Args:
            name: the label of value.
            value: what is to be validated.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
