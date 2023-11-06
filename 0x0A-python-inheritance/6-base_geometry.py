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
