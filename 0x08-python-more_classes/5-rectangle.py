#!/usr/bin/python3
"""
Defines a class Rectangle that represents a rectangle.

Attributes:
    width (int): Width of the rectangle.
    height (int): Height of the rectangle.
"""


class Rectangle:
    """
    Class that defines properties of a rectangle.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Creates new instances of Rectangle.

        Args:
            width (int, optional): Width of rectangle. Defaults to 0.
            height (int, optional): Height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width retriever."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter for width of rectangle.

        Args:
            value (int): Width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Height retriever."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter for height of rectangle.

        Args:
            value (int): Height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates Area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates Perimeter of the rectangle.

        Returns:
            int: Perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        result = ""
        if self.__width > 0 and self.__height > 0:
            for _ in range(self.__height):
                result += "#" * self.__width + "\n"
        return result[:-1]

    def __repr__(self):
        """Returns a representation of the rectangle."""
        object_address = hex(id(self))
        class_name = 'Rectangle'
        return "<{} object at {}>".format(class_name, object_address)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
