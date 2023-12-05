#!/usr/bin/python3

"""
A function to create a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file to load.

    Returns:
    object: The Python object created from the JSON file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return json.load(file)
     return my_obj
