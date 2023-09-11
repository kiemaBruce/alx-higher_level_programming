#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """Contains an instance method that raises an error."""

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
                ValueError: if value is not greater than 0.
        """
        if not type(value) is int:
            raise TypeError(f"{name:s} must be an integer")
        if value <= 0:
            raise ValueError(f"{name:s} must be greater than 0")
