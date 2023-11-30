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
    try:
        if not (isinstance(a, int)) and not isinstance(a, float):
            raise TypeError("a must be an integer")
        elif not (isinstance(b, int)) and not isinstance(b, float):
            raise TypeError("b must be an integer")
        else:
            if isinstance(a, float) or isinstance(b, float):
                return (int(a) + int(b))
            return a + b
    except Exception as e:
        return (e)
