#!/usr/bin/python3

"""
Check if the object is an instance of, or i\
        if it inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of, or \
            if it inherited from, the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The specified class to check against.

    Returns:
    True if obj is an instance of, or inherited from, a_class; otherwise, False
    """
    return isinstance(obj, a_class)
