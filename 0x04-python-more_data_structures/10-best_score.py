#!/usr/bin/python3
def best_score(a_dictionary):
    counter = 0
    if a_dictionary is None:
        return None
    for key in a_dictionary:
        value = a_dictionary.get(key)
        if counter == 0:
            return_key = key
            i = value
        else:
            if value > i:
                i = value
                return_key = key
        counter += 1
    return return_key
