#!/usr/bin/python3
"""
Module for writing a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    Function to write a string to a text file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return (file.write(text))
