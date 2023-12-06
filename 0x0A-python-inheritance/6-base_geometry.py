#!/usr/bin/python3
"""Raise exceptions on area"""


class BaseGeometry:
    """Class representing base geometry."""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")
