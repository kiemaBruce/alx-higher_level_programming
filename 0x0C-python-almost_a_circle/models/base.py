#!/usr/bin/python3
"""
Definition of the Base class.
"""

import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string.
        Args:
            json_string (str): a string representing a list of dictionaries.
        Return:
            list: the list represented by JSON string.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set.
        Args:
            dictionary: a dictionary that contains the attributes to be set.
        Return:
            instance: an instance with attributes already set using dictionary
        """
        from .rectangle import Rectangle
        from .square import Square
        for key in dictionary:
            if key == "size":
                s1 = Square(6)
                s1.update(**dictionary)
                return s1
                break
            elif key == "width" or key == "height":
                r1 = Rectangle(5, 7)
                r1.update(**dictionary)
                return r1
                break

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from a file.
        """
        filename = cls.__name__ + ".json"
        ret_list = []
        if not os.path.exists(filename):
            return ret_list
        with open(filename, "r", encoding="utf-8") as myfile:
            list_from_file = cls.from_json_string(myfile.read())
            for item in list_from_file:
                ret_list.append(cls.create(**item))
        return ret_list
