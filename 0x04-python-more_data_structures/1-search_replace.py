#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for index, value in enumerate(my_list):
        if value == search:
            new_list.insert(index, replace)
        else:
            new_list.append(value)
    return new_list
