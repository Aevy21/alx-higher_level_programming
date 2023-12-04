#!/usr/bin/python3

"""
checks if an object is an instance of a class that\
        inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that \
            otherwise False.

    Parameters:
    - obj: The object to be checked.
    - a_class: The specified class to check against.

    Returns:
    True if obj is an instance of a class that inherited from a_clas \
            otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
