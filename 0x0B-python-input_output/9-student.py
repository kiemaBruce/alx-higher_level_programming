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

    def to_json(self):
        """Returns the dictionary representation of a Student instance."""
        return self.__dict__
