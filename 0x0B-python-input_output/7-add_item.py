#!/usr/bin/python3
""" Adds all arguments to a Python list,
    and then saves them to a file
"""
from sys import argv
import json

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    # load the data from the 'add_item.json' file if it exists
    try:
        add_item_data = load_from_json_file("add_item.json")

        # concatenating the loaded data with the command-line arguments
        # excluding the script name
        loaded_data = add_item_data + argv[1:]

    # handle the case where the JSON file does not exist or is empty
    except (FileNotFoundError, json.JSONDecodeError):
        add_item_data = []
        loaded_data = argv[1:]

    save_to_json_file(loaded_data, "add_item.json")
