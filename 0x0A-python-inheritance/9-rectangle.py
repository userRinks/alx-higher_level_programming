#!/usr/bin/python3
"""Module that defines a Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherited from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
