#!/usr/bin/python3
"""
This module defines the Student class.
"""


class Student:
    """Definition of the methods that are associated with a Student object"""

    def __init__(self, first_name, last_name, age):
        """Initializes public instance variables
        Args:
                first_name: the first name of the Student.
                last_name: the last name of the Student.
                age: the age of the Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance.
        Args:
            list: a list of strings. Only the attributes that are contained in
            this list are to be returned in the dictionary representation of
            the instance.
        """
        if attrs is None:
            return self.__dict__
        index = 0
        ret_dict = dict()
        for key in attrs:
            if key in self.__dict__:
                ret_dict[key] = self.__dict__[key]
        return ret_dict
