#!/usr/bin/python3
"""
Adds two integers with Parameters:
    a (int or float): The first parameter.
    b (int or float, optional): The second parameter. Defaults to 98.
"""


def add_integer(a, b=98):
    """
    Returns - int: The sum of a and b.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
