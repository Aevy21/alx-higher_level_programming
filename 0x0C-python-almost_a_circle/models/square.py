#!/usr/bin/python3
"""
Square class, inherits from Rectangle.
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of the square, else x=0.
            y (int, optional): Y-coordinate of the square , else y=0.
            id (int, optional): If provided, assigns the given ID or id=None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns attr to the Square instance using a list.

        Args:
            *args: List of arguments (id, size, x, y).
            **kwargs: Dictionary of keyworded arguments.

        Note:
            **kwargs must be skipped if *args exists and is not empty.
        """
        attr_names = ["id", "size", "x", "y"]
        if args:
            attrs = args
        elif kwargs:
            attrs = [kwargs.get(attr, getattr(self, attr)) for attr in attr_names]
        else:
            return

        for i, attribute in enumerate(attribute_names):
            if i < len(attributes):
                setattr(self, attribute, attributes[i])

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        coords_str = "{}/{}".format(self.x, self.y)
        return "[Square] ({}) {} - {}".format(self.id, coords_str, self.width)
