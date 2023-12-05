#!/usr/bin/python3
""" Adds all arguments to a Python list,
    and then saves them to a file
"""
from sys import argv
import json

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file

    try:
        # Try loading data from the 'add_item.json' file
        loaded_data = load_from_json_file("add_item.json")

    except (FileNotFoundError, json.JSONDecodeError):
        # Handle the case where the file doesn't exist or is empty
        loaded_data = []

    # Concatenate loaded data with command-line args(excluding script name)
    loaded_data += argv[1:]

    # Save the combined data back to the 'add_item.json' file
    save_to_json_file(loaded_data, "add_item.json")
