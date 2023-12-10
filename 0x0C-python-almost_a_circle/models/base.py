#!/usr/bin/python3
"""
a Base with a private class attr
"""


class Base:
    """

    Attributes:
    __nb_objects (int): Private class attr to keep track of the num of objects.
    id (int): Public instance attr representing the object's ID.
    """

    __nb_objects = 0  # private class attr

    def __init__(self, id=None):
        """
        Args:
            id (int, optional): If provided, assigns the given ID. \
                    If None, auto-increments the ID.

        Note:
            If id is not provided, it will be auto generated\
                    using the __nb_objects counter.
        """
        if id is not None:
            self.id = id  # assign id if provided
        else:
            Base.__nb_objects += 1  # increment class attr
            self.id = Base.__nb_objects  # assign the new value to id
