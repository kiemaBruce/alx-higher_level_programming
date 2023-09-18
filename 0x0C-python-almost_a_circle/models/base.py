#!/usr/bin/python3
"""
Definition of the Base class.
"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_s = json.dumps(list_dictionaries)
        return json_s
