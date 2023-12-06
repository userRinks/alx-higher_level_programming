#!/usr/bin/python3
"""
Module for dict description for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Function to get the dictionary description for obj JSON serialization

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary description of obj for JSON serialization
    """
    # Get a dictionary representation of the object's __dict__ attribute
    return obj.__dict__
