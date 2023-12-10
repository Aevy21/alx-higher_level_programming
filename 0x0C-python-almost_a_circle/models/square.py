#!/usr/bin/python33
"""
    Square class, inherits from Rectangle.
"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """
        Initializes a new instance of the Square class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.
        """
        coords_str = "{}/{}".format(self.x, self.y)
        return "[Square] ({}) {} - {}".format(self.id, coords_str, self.width)
