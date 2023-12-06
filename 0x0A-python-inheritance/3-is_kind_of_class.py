#!/usr/bin/python3

"""
Check if an object is an instance of, or inherited from, a class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of/inherited from a specified class

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to compare against.

    Returns:
        bool: True if obj is an instance/inheritance of a_class;
        False otherwise.
    """

    return isinstance(obj, a_class)
