#!/usr/bin/python3
"""
Note: This is a class that defines a rectangle
"""


class Rectangle:
    """
    Rectangle Class:

    This class defines a rectangle with private attributes width and height.
    It includes getters and setters for width and height, enforcing
    type checking and non-negativity. It also has methods to calculate
    the area and perimeter of the rectangle.

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

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
    if self._width > 0 and self._height > 0:
        return 2 * (self._width + self._height)
    else:
        return 0
