#!/usr/bin/python3
"""
A function that list all  of available attributes and methods of an object
"""


def lookup(obj):
    """Returns a list of attributes and methods of an object."""

    result = []
    for attribute_name in dir(obj):
        if not callable(getattr(obj, attribute_name)):
            result.append(attribute_name)
    return result
