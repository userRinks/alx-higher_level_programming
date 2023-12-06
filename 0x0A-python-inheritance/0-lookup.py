#!/usr/bin/python3
"""
This module defines a function lookup
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: An object.

    Returns:
        A list of attribute and method names.

    """
    return dir(obj)
