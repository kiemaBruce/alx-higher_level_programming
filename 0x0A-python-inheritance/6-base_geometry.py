#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """Contains an instance method that raises an error."""

    def area(self):
        """Raises an exception."""
        raise Exception("area() is not implemented")
