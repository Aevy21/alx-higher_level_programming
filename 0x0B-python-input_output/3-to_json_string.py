#!/usr/bin/python3

"""
a function to convert an object to its JSON representation
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Parameters:
    - my_obj: The object to be converted to JSON.

    Returns:
    str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
