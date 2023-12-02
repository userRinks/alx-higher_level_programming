#!/usr/bin/python3
"""Module containing the definition of the Square class."""


class Square:
    """
    Defines a square.

    Attributes:
        __size (number): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (number): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute.

        Returns:
            number: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.

        Parameters:
            value (number): The new size value.

        Raises:
            TypeError: If the value is not a number (float or integer).
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            number: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison based on the area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Inequality comparison based on the area."""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Less than comparison based on the area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Less than or equal to comparison based on the area."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """Greater than comparison based on the area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Greater than or equal to comparison based on the area."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
