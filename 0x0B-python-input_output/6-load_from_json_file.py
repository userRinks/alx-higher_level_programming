#!/usr/bin/python3
"""
Module for creating an Object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    Function to create an Object from a JSON file

    Args:
        filename (str): The name of the JSON file

    Returns:
        obj: The Python object created from the JSON file
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
