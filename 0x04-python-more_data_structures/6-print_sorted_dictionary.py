#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_list = list(a_dictionary.keys())
    (keys_list).sort()
    for i in keys_list:
        print("{:s}: {}".format(i, a_dictionary.get(i)))
