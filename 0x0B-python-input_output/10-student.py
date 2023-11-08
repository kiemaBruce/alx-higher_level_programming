#!/usr/bin/python3
"""Contains Student class.
"""


class Student:
    """Methods and attributes of a Student object."""

    def __init__(self, first_name, last_name, age):
        """Initializes Student object.
        Args:
                first_name (str): student's first name.
                last_name (str): student's last name.
                age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of Student instance.
        Args:
                attrs (list): a list of strings. The strings are the only
                attributes of the object that are to be retrieved.
        """
        ret_dict = dict()
        attrs_all = dir(self)
        c = 1
        if type(attrs) is list:
            for i in attrs:
                if type(i) is str:
                    c = 0
                elif type(i) is not str:
                    c = 1
        if c == 0:
            filter_set = set(attrs)
            for i in attrs_all:
                if (
                    not i.startswith("__")
                    and not callable(getattr(self, i))
                    and i in filter_set
                ):
                    ret_dict[i] = getattr(self, i)
        elif c == 1:
            for i in attrs_all:
                if not i.startswith("__") and not callable(getattr(self, i)):
                    ret_dict[i] = getattr(self, i)
        return ret_dict
