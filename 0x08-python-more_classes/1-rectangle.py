#!/usr/bin/python3
"""
Note: This is a class that defines a rectangle
"""


class Rectangle:
    """
    Rectangle Class:

    This class defines a rectangle with width and height attributes.
    It includes getters and setters for width and height, enforcing
    type checking and non-negativity.

    Attributes:
    - _width (int): Width of the rectangle.
    - _height (int): Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Parameters:
        - width (int, optional): Width of the rectangle (default is 0).
        - height (int, optional): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Parameters:
        - value (int): New width value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Parameters:
        - value (int): New height value.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
        
     def __repr__(self):
        """Return a string representation to recreate a new instance."""
        return "{{'_Rectangle__width': {}, '_Rectangle__height': {}}}".format(self._width, self._height)
         
