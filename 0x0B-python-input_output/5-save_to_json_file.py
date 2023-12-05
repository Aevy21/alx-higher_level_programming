#!/usr/bin/python3

"""
A function to write a Python object to a text file using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using a JSON representation.

    Parameters:
    - my_obj: The Python object to be serialized and written to the file.
    - filename (str): The name of the file to save the JSON data.

    Returns:
    None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
