#!/usr/bin/python3

"""
A function to return the dictionary description for\
        JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    Parameters:
    - obj: An instance of a Class with serializable attributes.

    Returns:
    dict: The dictionary description for JSON serialization.
    """
    attributes = vars(obj)
    serializable_attributes = {
        key: value for key, value in attributes.items()
        if isinstance(value, (list, dict, str, int, bool))
    }

    return serializable_attributes
