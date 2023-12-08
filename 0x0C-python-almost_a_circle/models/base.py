 #!/usr/bin/python3
"""
a class Base with a private class attribute __nb_objects and a constructor that either assigns the provided id \
        or increments the class attribute to generate a new value for the public instance attribute id.
"""

class Base:
    """
    
    Attributes:
        __nb_objects (int): Private class attribute to keep track of the number of objects.
        id (int): Public instance attribute representing the object's ID.
    """

    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """
        Args:
            id (int, optional): If provided, assigns the given ID. If None, auto-increments the ID.

        Note:
            If id is not provided, it will be automatically generated using the __nb_objects counter.
        """
        if id is not None:
            self.id = id  # assign id if provided
        else:
            Base.__nb_objects += 1  # increment class attribute
            self.id = Base.__nb_objects  # assign the new value to id
