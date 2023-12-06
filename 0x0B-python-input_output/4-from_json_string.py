#!/usr/bin/python3
"""
Module for returning an object represented by a JSON string.
"""

import json


def from_json_string(my_str):
    """
    Function to return an object represented by a JSON string.

    Args:
        my_str (str): The JSON-formatted string.

    Returns:
        obj: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
