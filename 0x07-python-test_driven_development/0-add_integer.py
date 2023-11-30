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
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
