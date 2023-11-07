#!/usr/bin/python3
"""Contains the definition of the class_to_json() function.
"""


def class_to_json(obj):
    """Returns a dictionary containing an object's attributes.
    Args:
            obj: the object whose attributes are to be returned.
    """
    my_list = dir(obj)
    ret_dict = dict()
    for i in my_list:
        if not i.startswith("__") and not callable(getattr(obj, i)):
            ret_dict[i] = getattr(obj, i)
    return ret_dict
