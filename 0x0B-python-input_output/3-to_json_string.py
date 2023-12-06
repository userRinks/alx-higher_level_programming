#!/usr/bin/python3
"""
Module for returning the JSON representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    Function to return the JSON representation of an object.

    Args:
        my_obj (obj): The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
