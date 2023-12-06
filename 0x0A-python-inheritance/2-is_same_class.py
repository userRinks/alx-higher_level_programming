#!/usr/bin/python3

"""
Module to check if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """

    return type(obj) is a_class
