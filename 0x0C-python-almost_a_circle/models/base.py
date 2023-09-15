#!/usr/bin/python3
"""
Definition of the Base class.
"""


class Base:
    """Defines the Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the id.
        Args:
                id (int): the id.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
