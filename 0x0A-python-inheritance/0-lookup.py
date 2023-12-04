#!/usr/bin/python3
"""
A function that list all  of available attributes and methods of an object
"""


def lookup(obj):
    """Returns a list of attributes and methods of an object."""
    return [attribute_name for attribute_name in dir(obj)]
