#!/usr/bin/python3
"""Definition of Student class.
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

    def to_json(self):
        """Returns a dictionary representation of Student instance."""
        ret_dict = dict()
        attrs = dir(self)
        for i in attrs:
            if not i.startswith("__") and not callable(getattr(self, i)):
                ret_dict[i] = getattr(self, i)
        return ret_dict
