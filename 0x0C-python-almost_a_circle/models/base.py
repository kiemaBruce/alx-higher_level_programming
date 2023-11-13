#!/usr/bin/python3
"""Contains definition of Base class. Manages assignment of instance id
attribute.
"""


import json


class Base:
    """The attributes and methods of the Base class.
    Attributes:
            __nb_objects (int): the number of class instances that have been
                                created without an id being provided.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes class attributes.
        Args:
                id (int): used to initialize the id of the instance if
                          it isn't None.
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries
        Args:
            list_dictionaries (list): a list of dictionaries.
        Returns:
            JSON string: the JSON representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
