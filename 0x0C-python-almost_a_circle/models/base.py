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
        Args:
            list_dictionaries (list): a list of dictionaries.
        Return:
            str: the JSON string equivalent of list_dictionaries. If
            list_dictionaries is None or empty "[]" is returned.
        """
        ret_list = []
        if list_dictionaries is not None and len(list_dictionaries) != 0:
            for item in list_dictionaries:
                try:
                    item.to_dictionary()
                except AttributeError:
                    ret_list.append(item)
                else:
                    ret_list.append(item.to_dictionary())
        return json.dumps(ret_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list):  a list of instances who inherits of Base -
            example: list of Rectangle or list of Square instances.
        """
        filename = cls.__name__ + ".json"
        json_s = cls.to_json_string(list_objs)
        with open(filename, "w", encoding="utf-8") as myfile:
            myfile.write(json_s)
