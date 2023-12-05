#!/usr/bin/python3
"""
This module has a script that calls on two other modules
to load, add and save to file
"""


import sys
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# load list from the file
myList = load_from_json_file("add_item.json")

# add command line arguments to list
myList.extend(sys.argv[1:])

# save the list to the file
save_to_json_file(myList, "add_item.json")
