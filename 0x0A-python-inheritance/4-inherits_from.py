#!/usr/bin/python3
"""
Check if an object is an instance of an inherited class.
"""


def inherits_from(obj, a_class):
    """
    Check if object is instance of a class inherited from specific class

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to compare against.

    Returns:
        bool:
        True if obj is an instance of a class that inherited from a_class
        False otherwise.
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
