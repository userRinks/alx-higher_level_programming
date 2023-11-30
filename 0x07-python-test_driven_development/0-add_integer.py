#!/usr/bin/python3
"""
add_integer: Adds two integers with Parameters:
    a (int or float): The first parameter.
    b (int or float, optional): The second parameter. Defaults to 98.
"""


def add_integer(a, b=98):
    """
    Returns - int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
