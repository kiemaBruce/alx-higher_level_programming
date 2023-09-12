#!/usr/bin/python3
import sys
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


"""
This module adds all arguments to it into a Python List and then saves them
into a file. The file is saved in JSON format.
"""


filename = "add_item.json"
for index, value in enumerate(sys.argv):
    try:
        myfile = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        items = []
    else:
        items = load_from_json_file(filename)
    finally:
        if index != 0:
            items.append(value)
        save_to_json_file(items, filename)
