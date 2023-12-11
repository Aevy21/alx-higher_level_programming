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
            y (int, optional): Y-coordinate of the rectangle or y=0.
            id (int, optional): If provided, assigns the given ID.or id=None.
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
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
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
        cod_str variable for coodinates
        dim_str variable for dimensions attrubutes
        """
        cod_str = "{}/{}".format(self.__x, self.__y)
        dim_str = "{}/{}".format(self.__width, self.__height)
        rect_str = "[Rectangle] ({}) {} - {}".format(self.id, cod_str, dim_str)
        return rect_str

    def display(self):
        """
        Prints the Rectangle instance with '#' characters, considering x and y.
        """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Updates the values of a Rectangle instance attributes"""
        attributes_list = ["id", "width", "height", "x", "y"]

        for i in range(len(args)):
            setattr(self, attributes_list[i], args[i])

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.
        """
        attributes = ('id', 'width', 'height', 'x', 'y')
        return {attr: getattr(self, attr) for attr in attributes}
