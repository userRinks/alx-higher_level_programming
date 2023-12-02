#!/usr/bin/python3
"""Module containing the definition of the Square class"""


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
