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

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """ retrive the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width if all test conditions are met """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the heigt if all conditions are met """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
