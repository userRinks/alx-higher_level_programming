#!/usr/bin/python3
"""Module containing the definition of the MagicClass class."""
import math


class MagicClass:
    """
    A class that performs similar operations as described in
        the provided Python bytecode.

    Attributes:
        __radius (number): The radius of the circle.
    """
    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass class.

        Parameters:
            radius (number): The radius of the circle. Defaults to 0.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Computes and returns the area of the circle.

        Returns:
            number: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Computes and returns the circumference of the circle.

        Returns:
            number: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
