#!/usr/bin/python3
"""
Module for writing an Object to a text file using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Function to write an Object to a text file using a JSON representation

    Args:
        my_obj (obj): object to be serialized to JSON.
        filename (str): name of file to save the JSON representation.

    Returns:
        None
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
