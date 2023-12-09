#!/usr/bin/python3
"""
   Creating a Rectangle class, inherits from Base.
"""

from models.base import Base

class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
        __width (int): Private width attribute.
        __height (int): Private height attribute.
        __x (int): Private x attribute.
        __y (int): Private y attribute.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle. Defaults to 0.
            y (int, optional): Y-coordinate of the rectangle. Defaults to 0.
            id (int, optional): If provided, assigns the given ID. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("X must be an integer")
        if value < 0:
            raise ValueError("X must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("Y must be an integer")
        if value < 0:
            raise ValueError("Y must be >= 0")
        self.__y = value

    def area(self):
        # Calculate and return the area
        return self.__width * self.__height

    def display(self):
        # Display the rectangle with '#' character
        for _ in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """
        coords_str = "{}/{}".format(self.__x, self.__y)
        return "[Rectangle] ({}) {} - {}/{}".format(self.id, coords_str, self.__width, self.__height)

    def display(self):
        """
        Prints the Rectangle instance with '#' characters, considering x and y.
        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)


    def update(self, *args):
        """
        Assigns arguments to the Rectangle attributes in the specified order.

        Args:
            *args: Arguments to assign in the order: id, width, height, x, y.
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
