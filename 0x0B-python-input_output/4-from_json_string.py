#!/usr/bin/python3

"""
A function to convert a JSON string to a Python object.
"""

import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Parameters:
    - my_str (str): The JSON-formatted string.

    Returns:
    object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
