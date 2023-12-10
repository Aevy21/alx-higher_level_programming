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
            x (int, optional): X-coordinate of the square. Defaults to 0.
            y (int, optional): Y-coordinate of the square oherwise y=0.
            id (int, optional): If provided, assigns the given ID, or d=None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): New size value.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        coords_str = "{}/{}".format(self.x, self.y)
        return "[Square] ({}) {} - {}".format(self.id, coords_str, self.width)
