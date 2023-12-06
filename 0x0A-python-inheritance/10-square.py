#!/usr/bin/python3
"""Module that defines a Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherited from Rectangle."""

    def __init__(self, size):
        """Initialize a Square instance."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the square description."""
        return "[Rectangle] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height
        )
