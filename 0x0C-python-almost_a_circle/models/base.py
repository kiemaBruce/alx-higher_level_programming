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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): a list of instances who inherits of Base -
                              example: list of Rectangle or list of
                              Square instances. If list_objs is None, an empty
                              list is saved. The filename is <Class name>.json
                              for example: Rectangle.json
        """
        if list_objs is None:
            filename = list_objs.__class__.__name__ + ".json"
            with open(filename, mode="w", encoding="utf-8") as myfile:
                myfile.write('[]')
        else:
            dict_list = []
            if len(list_objs) != 0:
                for item in list_objs:
                    dict_list.append(item.to_dictionary())
                dict_list_json = cls.to_json_string(dict_list)
                filename = list_objs[0].__class__.__name__ + ".json"
                with open(filename, mode="w", encoding="utf-8") as myfile:
                    myfile.write(dict_list_json)
