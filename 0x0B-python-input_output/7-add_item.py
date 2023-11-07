#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file.
"""


import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


filename = "add_item.json"
try:
    with open(filename, mode="r+", encoding="utf-8") as my_file:
        if my_file.read() == "":
            my_list = []
        else:
            # Assuming that if the file isn't empty then it cannot contain
            # anything other than a list.
            my_list = load_from_json_file(filename)
except FileNotFoundError as e:
    with open(filename, mode="w", encoding="utf-8") as new_file:
        my_list = []
for i in range(len(sys.argv)):
    if i > 0:
        my_list.append(sys.argv[i])
save_to_json_file(my_list, filename)
